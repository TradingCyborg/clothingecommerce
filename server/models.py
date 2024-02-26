from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

# One-to-One Relationship
class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    phone = db.Column(db.String(14), unique=True)
    password = db.Column(db.String(450), nullable=False)
    address = db.Column(db.String(70), nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Customer Item {self.name}>'
    
    @validates("name")
    def validate_names(self, key, name):
        if not name:
            raise ValueError('Name Field is required')
        return name
    
    @validates("email")
    def validate_email(self, key, value):
        if '@' not in value:
            raise ValueError('Please enter a valid email')
        return value
    

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti =  db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(85), nullable=False)
    imageUrl = db.Column(db.Text, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Item {self.name}, {self.price}, {self.description}, {self.category}, {self.imageUrl}, {self.size}>'
    
    


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.DateTime(), server_default=db.func.now())
    price = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))
    product = db.relationship("Product", backref=db.backref('order', lazy=True), cascade="all, delete")

    
class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    customer = db.relationship("Customer", backref=db.backref('reviews', lazy=True), cascade="all, delete-orphan", single_parent=True)
    product = db.relationship("Product", backref=db.backref('reviews', lazy=True), cascade="all, delete-orphan", single_parent=True)


    @validates("rating")
    def validate_rating(self, key, value):
        if value < 0 or value > 6:
            raise ValueError('Please provide a value between 0 and 6')
        return value




