# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Association Table for many-to-many relationship between Product and Order
product_order_association = db.Table(
    'product_order_association',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
)

cart_product_association = db.Table(
    'cart_product_association',
    db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'))
)

class TokenBlocklist(db.Model):
    __tablename__ = 'token_blocklist'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"<TokenBlocklist {self.id} {self.token}>"

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)

    user = db.relationship("User", back_populates="profile")
    customer_reviews = db.relationship("Review", back_populates="user_profile", lazy=True, cascade="all, delete-orphan", single_parent=True)
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    full_name = db.Column(db.String(100))  # New attribute

    profile = db.relationship("UserProfile", back_populates="user", uselist=False)

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', back_populates='category')

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    imageUrl = db.Column(db.String(255))
    size = db.Column(db.Integer)  # Added size attribute

    category = db.relationship("Category", back_populates="products")
    orders = db.relationship("Order", secondary=product_order_association, back_populates="products")
    reviews = db.relationship("Review", back_populates="product")
    carts = db.relationship('Cart', secondary=cart_product_association, back_populates='products')
    reviews_product = db.relationship("Review", back_populates="product", overlaps="reviews")

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    password_hash = db.Column(db.String(128))

    created_at = db.Column(db.DateTime, default=db.func.now())

    carts = db.relationship('Cart', back_populates='customer')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Invalid email address')
        return email

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.DateTime, server_default=db.func.now())
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    products = db.relationship("Product", secondary=product_order_association, back_populates="orders")
    customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"<Order {self.id} - {self.customer.name} - {self.product.name}>"

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profiles.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    user_profile = db.relationship("UserProfile", back_populates="customer_reviews", lazy=True, cascade="all, delete-orphan", single_parent=True)
    product = db.relationship("Product", back_populates="reviews")

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)
    total_price = db.Column(db.Float, nullable=False)
    delivery_address = db.Column(db.String(100))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    customer = db.relationship('Customer', back_populates='carts')
    products = db.relationship('Product', secondary=cart_product_association, back_populates='carts')


