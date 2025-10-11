from flask import Flask, render_template, request
from config import Config
from models import db
from models.product import Product

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

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
    categories = sorted(categories)
    return render_template('index.html', products=products, categories=categories, q=q, selected_category=category)

if __name__ == '__main__':
    app.run(debug=True)