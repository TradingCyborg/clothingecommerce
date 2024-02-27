


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Text, func, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(70), unique=True, nullable=False)
    phone = Column(String(14), unique=True)
    password = Column(String(450), nullable=False)
    address = Column(String(70), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    carts = relationship('Cart', back_populates='customer')
    profile = relationship('Profile', back_populates='customer', uselist=False)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    bio = Column(Text)
    image_url = Column(String(255))
    customer_id = Column(Integer, ForeignKey('customers.id'), unique=True)
    customer = relationship('Customer', back_populates='profile', uselist=False)

class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    products = relationship('Product', back_populates='category')

class Cart(db.Model):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Float, nullable=False)
    delivery_address = Column(String(100))
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    customer = relationship('Customer', back_populates='carts')
    products = relationship("Product", secondary="cart_product_association", back_populates="carts")

class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(85), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    imageUrl = Column(Text, nullable=False)
    size = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    category = relationship('Category', back_populates='products')
    carts = relationship("Cart", secondary="cart_product_association", back_populates="products")




class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    orderdate = Column(DateTime, server_default=func.now())
    price = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    product_id = Column(Integer(), ForeignKey('products.id'))
    customer = relationship("Customer", backref='orders', lazy=True)
    products = relationship("Product", backref='orders', lazy=True)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    customer = relationship("Customer", backref="customer_reviews", lazy=True)
    products = relationship("Product", backref="reviews_product", lazy=True)


class CartProductAssociation(db.Model):
    __tablename__ = 'cart_product_association'
    id = Column(Integer, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)

    carts = relationship("Cart", backref="products_associated")
    products = relationship("Product", backref="carts_associated")

    __table_args__ = (
        UniqueConstraint('cart_id', 'product_id', name='uq_cart_product'),
    )






class TokenBlocklist(db.Model):
    __tablename__ = 'token_blocklist'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, jti):
        self.jti = jti


