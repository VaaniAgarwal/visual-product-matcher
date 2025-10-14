from app import app
from models import db
from models.product import Product
import json

sample_products = [
    # ---- Clothing ----
    {"name": "Red T-Shirt", "category": "Clothing", "image_url": "static/images/red_tshirt.jpg", "embedding": []},
    {"name": "Blue Jeans", "category": "Clothing", "image_url": "static/images/blue_jeans.jpg", "embedding": []},
    {"name": "Black Shirt", "category": "Clothing", "image_url": "static/images/black_shirt.jpg", "embedding": []},
    {"name": "Black Hoodie", "category": "Clothing", "image_url": "static/images/black_hoodie.jpeg", "embedding": []},
    {"name": "Yellow Summer Dress", "category": "Clothing", "image_url": "static/images/yellow_summer_dress.jpeg", "embedding": []},
    {"name": "Grey Sweater", "category": "Clothing", "image_url": "static/images/grey_sweater.jpeg", "embedding": []},
    {"name": "Denim Jacket", "category": "Clothing", "image_url": "static/images/denim_jacket.jpeg", "embedding": []},
    {"name": "Green Kurti", "category": "Clothing", "image_url": "static/images/green_kurti.jpeg", "embedding": []},
    {"name": "Formal Blazer", "category": "Clothing", "image_url": "static/images/formal_blazer.jpg", "embedding": []},
    {"name": "Printed Skirt", "category": "Clothing", "image_url": "static/images/printed_skirt.jpg", "embedding": []},

    # ---- Footwear ----
    {"name": "Running Shoes", "category": "Footwear", "image_url": "static/images/running_shoes.jpeg", "embedding": []},
    {"name": "Leather Boots", "category": "Footwear", "image_url": "static/images/leather_boots.jpeg", "embedding": []},
    {"name": "Casual Sneakers", "category": "Footwear", "image_url": "static/images/casual_sneakers.jpg", "embedding": []},
    {"name": "High Heels", "category": "Footwear", "image_url": "static/images/high_heels.jpeg", "embedding": []},
    {"name": "Flip Flops", "category": "Footwear", "image_url": "static/images/flip_flops.jpeg", "embedding": []},
    {"name": "Sports Sandals", "category": "Footwear", "image_url": "static/images/sports sandals.jpeg", "embedding": []},
    {"name": "Formal Shoes", "category": "Footwear", "image_url": "static/images/formal_shoes.jpeg", "embedding": []},
    {"name": "Loafers", "category": "Footwear", "image_url": "static/images/loafers.jpeg", "embedding": []},
    {"name": "Ballet Flats", "category": "Footwear", "image_url": "static/images/ballet_flats.jpeg", "embedding": []},
    {"name": "Ankle Boots", "category": "Footwear", "image_url": "static/images/ankle_boots.jpeg", "embedding": []},

    # ---- Accessories ----
    {"name": "Leather Belt", "category": "Accessories", "image_url": "static/images/leather_belt.jpeg", "embedding": []},
    {"name": "Black Sunglasses", "category": "Accessories", "image_url": "static/images/black_sunglasses.jpeg", "embedding": []},
    {"name": "Silver Watch", "category": "Accessories", "image_url": "static/images/silver_watch.jpeg", "embedding": []},
    {"name": "Gold Necklace", "category": "Accessories", "image_url": "static/images/gold_necklace.jpg", "embedding": []},
    {"name": "Wool Scarf", "category": "Accessories", "image_url": "static/images/wool_scarf.jpeg", "embedding": []},
    {"name": "Baseball Cap", "category": "Accessories", "image_url": "static/images/baseball_cap.jpeg", "embedding": []},
    {"name": "Stud Earrings", "category": "Accessories", "image_url": "static/images/stud_earrings.jpeg", "embedding": []},
    {"name": "Travel Backpack", "category": "Accessories", "image_url": "static/images/travel_backpack.jpeg", "embedding": []},
    {"name": "Wallet", "category": "Accessories", "image_url": "static/images/wallet.jpeg", "embedding": []},
    {"name": "Hairband", "category": "Accessories", "image_url": "static/images/hairband.jpeg", "embedding": []},

    # ---- Electronics ----
    {"name": "Wireless Earbuds", "category": "Electronics", "image_url": "static/images/wireless_earbuds.jpeg", "embedding": []},
    {"name": "Bluetooth Speaker", "category": "Electronics", "image_url": "static/images/bluetooth_speaker.jpeg", "embedding": []},
    {"name": "Smartphone", "category": "Electronics", "image_url": "static/images/smartphone.jpg", "embedding": []},
    {"name": "Smartwatch", "category": "Electronics", "image_url": "static/images/smartwatch.jpeg", "embedding": []},
    {"name": "Laptop", "category": "Electronics", "image_url": "static/images/laptop.jpeg", "embedding": []},
    {"name": "Tablet", "category": "Electronics", "image_url": "static/images/tablet.jpeg", "embedding": []},
    {"name": "Digital Camera", "category": "Electronics", "image_url": "static/images/digital_camera.jpeg", "embedding": []},
    {"name": "Wireless Mouse", "category": "Electronics", "image_url": "static/images/wireless_mouse.jpeg", "embedding": []},
    {"name": "Keyboard", "category": "Electronics", "image_url": "static/images/keyboard.jpeg", "embedding": []},
    {"name": "Power Bank", "category": "Electronics", "image_url": "static/images/powerbank.jpg", "embedding": []},

    # ---- Home & Living ----
    {"name": "Table Lamp", "category": "Home", "image_url": "static/images/table_lamp.jpg", "embedding": []},
    {"name": "Cushion Cover", "category": "Home", "image_url": "static/images/cusion_cover.jpg", "embedding": []},
    {"name": "Wall Clock", "category": "Home", "image_url": "static/images/wall_clock.jpeg", "embedding": []},
    {"name": "Decor Vase", "category": "Home", "image_url": "static/images/decor_vase.jpeg", "embedding": []},
    {"name": "Floor Mat", "category": "Home", "image_url": "static/images/floor_mat.jpeg", "embedding": []},
    {"name": "Curtains", "category": "Home", "image_url": "static/images/curtains.jpeg", "embedding": []},
    {"name": "Photo Frame", "category": "Home", "image_url": "static/images/photo_frame.jpg", "embedding": []},
    {"name": "Wall Art", "category": "Home", "image_url": "static/images/wall_art.jpeg", "embedding": []},
    {"name": "Table Clock", "category": "Home", "image_url": "static/images/table_clock.jpeg", "embedding": []},
    {"name": "Artificial Plant", "category": "Home", "image_url": "static/images/artificial_plant.jpeg", "embedding": []},
]

with app.app_context():
    db.session.query(Product).delete()
    for item in sample_products:
        product = Product(
            name=item["name"],
            category=item["category"],
            image_url=item["image_url"],
            embedding=json.dumps(item["embedding"])
        )
        db.session.add(product)
    db.session.commit()
    print(f"{len(sample_products)} products added to the database!")
