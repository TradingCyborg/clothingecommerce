from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Define the many-to-many association table
cart_product_association = db.Table(
    'cart_product_association',
    db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.UniqueConstraint('cart_id', 'product_id', name='uq_cart_product')
)

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
    reviews = db.relationship("Review", backref="customer_reviews", lazy=True)
    profile = db.relationship("Profile", uselist=False, backref="customer", lazy=True)

    def __repr__(self):
        return f'<Customer Item {self.name}>'

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

    products = db.relationship('Product', back_populates='category')

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

    category = db.relationship('Category', back_populates='products')

    carts = db.relationship("Cart", backref="product", lazy=True, secondary=cart_product_association)
    reviews = db.relationship("Review", backref="product_reviews", lazy=True)

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

    products = db.relationship("Product", backref="cart", lazy=True, secondary=cart_product_association)

    def __repr__(self):
        return f'<Cart for Customer {self.customer_id}>'

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.DateTime(), server_default=db.func.now())
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))

    customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))
    order_products = db.relationship("Product", backref=db.backref('order', lazy=True), cascade="all, delete")

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

    @validates("rating")
    def validate_rating(self, key, value):
        # Modify the validation logic based on your requirements
        if value < 0 or value > 5:
            raise ValueError('Please provide a value between 0 and 5')
        return value

    customer = db.relationship("Customer", backref="customer_reviews", lazy=True, cascade="all, delete-orphan", single_parent=True)
    product = db.relationship("Product", backref="reviews_product", lazy=True, cascade="all, delete-orphan", single_parent=True)
