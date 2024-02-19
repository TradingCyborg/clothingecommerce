from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    phone = db.Column(db.String(14), unique=True)
    password = db.Column(db.String(450), nullable=False)
    address = db.Column(db.String(70), nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    carts = db.relationship("Cart", backref="customer", lazy=True)
    reviews = db.relationship("Review", backref="customer", lazy=True)
    profile = db.relationship("Profile", uselist=False, backref="customer", lazy=True)  # One-to-One relationship

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

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), unique=True)

    def __repr__(self):
        return f'<Profile for Customer {self.customer_id}>'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    products = db.relationship("Product", backref="category", lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    imageUrl = db.Column(db.Text, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    category = db.relationship("Category", backref="products", lazy=True)

    carts = db.relationship("Cart", backref="product", lazy=True, secondary="cart_product_association")  # Many-to-Many relationship
    reviews = db.relationship("Review", backref="product", lazy=True)

    def __repr__(self):
        return f'<Item {self.name}, {self.price}, {self.description}, {self.category.name}, {self.imageUrl}, {self.size}>'

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)
    total_price = db.Column(db.Float, nullable=False)
    delivery_address = db.Column(db.String(100))

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

    products = db.relationship("Product", backref="cart", lazy=True, secondary="cart_product_association")  # Many-to-Many relationship

    def __repr__(self):
        return f'<Cart for Customer {self.customer_id}>'

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    customer = db.relationship("Customer", backref=db.backref('reviews', lazy=True), cascade="all, delete-orphan", single_parent=True)
    product = db.relationship("Product", backref=db.backref('reviews', lazy=True), cascade="all, delete-orphan", single_parent=True)

    @validates("rating")
    def validate_rating(self, key, value):
        if value < 0 or value > 6:
            raise ValueError('Please provide a value between 0 and 6')
        return value
