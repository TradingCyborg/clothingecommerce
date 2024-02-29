from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

# User Model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    profile = db.relationship("UserProfile", uselist=False, back_populates="user")
    orders = db.relationship("Order", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")
    cart = db.relationship("Cart", uselist=False, back_populates="user")

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Invalid email address')
        return email

# One-to-One Relationship
class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255))

    user = db.relationship("User", back_populates="profile")

# One-to-Many Relationship
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    products = db.relationship("Product", back_populates="category")

# One-to-Many Relationship
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    image_url = db.Column(db.String(255)) 

    category = db.relationship("Category", back_populates="products")
    reviews = db.relationship("Review", back_populates="product")

# Many-to-Many Relationship
product_order_association = db.Table(
    'product_order_association',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
)

# Many-to-Many Relationship
product_cart_association = db.Table(
    'product_cart_association',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('cart_id', db.Integer, db.ForeignKey('carts.id'))
)

# Review Model
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    user = db.relationship("User", back_populates="reviews")
    product = db.relationship("Product", back_populates="reviews")

# Many-to-One Relationship
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=db.func.now())
    total_price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship("User", back_populates="orders")
    products = db.relationship("Product", secondary=product_order_association, back_populates="orders")

# One-to-One Relationship
class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship("User", back_populates="cart")
    products = db.relationship("Product", secondary=product_cart_association, back_populates="carts")


