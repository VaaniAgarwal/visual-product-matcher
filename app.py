from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from models.product import Product

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database tables created!")