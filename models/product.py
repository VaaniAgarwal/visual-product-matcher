from . import db
import json

class Product(db.Model):
    __tablename_ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    embedding = db.Column(db.Text, nullable=False)  # JSON string of image features

    def get_embedding(self):
        return json.loads(self.embedding)