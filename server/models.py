from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

#Remember to Serialize when all tables are added

db = SQLAlchemy()

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50),nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    phone = db.Column(db.String(14), unique=True)
    password = db.Column(db.String(450), unique=False,nullable=False)
    address = db.Column(db.String(70), unique=False, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Customer Item {self.firstname}>'
    
    @validates("firstname", "lastname")
    def validate_names(self,key,name):
        if not name:
            raise ValueError('Name Field is required')
        return name
    
    @validates("email")
    def validate_email(self,key,value):
        if '@' not in value:
            raise ValueError('Please enter a valid email')
        return value
    

    #   For Logout JWT Block List
class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti =  db.Column(db.String(100),nullable=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float,nullable=False)
    category = db.Column(db.String(85),nullable=False)
    imageUrl= db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer, nullable=(False))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Item {self.name}, {self.price}, {self.description}, {self.category}, {self.imageUrl},{self.quantity}>'
    
    


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
    products = db.relationship("Product", backref=db.backref('order', lazy=True), cascade="all, delete")



class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    paymentdate = db.Column(db.Integer, nullable=False)
    paymentmethod = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    
class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer,nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))

    customer = db.relationship("Customer", backref=db.backref('reviews', lazy=True), cascade="all, delete-orphan", single_parent=True)
    product = db.relationship("Product", backref=db.backref('reviews', lazy=True), cascade="all, delete-orphan", single_parent=True)



    @validates("rating")
    def validate_rating(self,key,value):
        if 0 > value > 6 not in value:
            raise ValueError('Please provide a value between 0 - 6')
        return value



    
class Favorite(db.Model, SerializerMixin):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))

    product = db.relationship("Product", backref=db.backref('favorites', lazy=True), cascade="all, delete")








