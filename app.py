import os
from flask import Flask, render_template, request
from config import Config
from models import db
from models.product import Product
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from hybrid_features import extract_hybrid_features

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

FEATURES_FILE = "data/image_features.pkl"

@app.route('/', methods=['GET'])
def home():
    q = request.args.get('q', '').strip()
    category = request.args.get('category', 'all').strip()
    query = Product.query
    if q:
        query = query.filter(Product.name.ilike(f"%{q}%"))
    if category and category.lower() != 'all':
        query = query.filter(Product.category == category)
    products = query.all()
    categories = [row[0] for row in db.session.query(Product.category).distinct().all()]
    return render_template('index.html', products=products, categories=categories, q=q, selected_category=category)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    similar_products = (
        Product.query.filter(Product.category == product.category, Product.id != product.id)
        .limit(4)
        .all()
    )
    return render_template('product_detail.html', product=product, similar_products=similar_products)

@app.route("/match", methods=["GET", "POST"])
def match_image():
    if request.method == "POST":
        file = request.files['image']
        image_url = request.form.get('image_url')
        upload_dir = "static/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        img_path = None
        filename = None

        if file and file.filename != '':
            filename = file.filename
            img_path = os.path.join(upload_dir, filename)
            file.save(img_path)
        
        elif image_url:
            import requests 
            from PIL import Image
            from io import BytesIO  
            try:
                response = requests.get(image_url, timeout=10)
                if response.status_code == 200:
                    filename = os.path.basename(image_url.split("?")[0])
                    img_path = os.path.join(upload_dir, filename)
                    image = Image.open(BytesIO(response.content))
                    image.save(img_path)
                else:
                    return "❌ Could not fetch image from URL."
            except Exception as e:
                return f"❌ Error loading image: {e}"
            
        else:
            return "⚠️ Please upload a file or provide an image URL."

        with open(FEATURES_FILE, "rb") as f:
            features = pickle.load(f)  
        query_vec = extract_hybrid_features(img_path).reshape(1, -1)
        similarities = {}
        for img_name, feat_vec in features.items():
            feat_vec = np.array(feat_vec).reshape(1, -1)
            sim = cosine_similarity(query_vec, feat_vec)[0][0]
            product = Product.query.filter(Product.image_url.contains(img_name)).first()
            if product and product.category == "Clothing":
                sim *= 1.1
            similarities[img_name] = sim

        top_imgs = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:5]
        similar_products = []
        for img_name, score in top_imgs:
            product = Product.query.filter(Product.image_url.contains(img_name)).first()
            if product:
                similar_products.append((product, score))
        return render_template('match_results.html', query_img=filename, similar_products=similar_products)

    return render_template('match_form.html')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
