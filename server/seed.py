# seed.py

from faker import Faker
from flask import Flask
from models import User, UserProfile, Category, Product, Review, Order, Cart, db

fake = Faker()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fentywear.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'
db.init_app(app)
db.app = app

def generate_fake_users(num_users):
    users = []
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        users.append(user)
    return users

def generate_fake_categories(num_categories):
    categories = []
    for _ in range(num_categories):
        category = Category(
            name=fake.word(),
        )
        categories.append(category)
    return categories

def generate_fake_products(num_products, categories):
    products = []
    for _ in range(num_products):
        product = Product(
            name=fake.word(),
            description=fake.text(),
            price=fake.random_float(min=1, max=100),
            stock_quantity=fake.random_int(min=1, max=100),
            category=fake.random_element(elements=categories),
            image_url=fake.image_url(),
        )
        products.append(product)
    return products

def generate_fake_reviews(num_reviews, users, products):
    reviews = []
    for _ in range(num_reviews):
        review = Review(
            rating=fake.random_int(min=1, max=5),
            comment=fake.text(),
            user=fake.random_element(elements=users),
            product=fake.random_element(elements=products),
        )
        reviews.append(review)
    return reviews

def generate_fake_orders(num_orders, users, products):
    orders = []
    for _ in range(num_orders):
        order = Order(
            order_date=fake.date_this_decade(),
            total_price=fake.random_float(min=10, max=500),
            user=fake.random_element(elements=users),
            products=fake.random_elements(elements=products, length=fake.random_int(min=1, max=5), unique=True),
        )
        orders.append(order)
    return orders

def generate_fake_carts(num_carts, users, products):
    carts = []
    for _ in range(num_carts):
        cart = Cart(
            user=fake.random_element(elements=users),
            products=fake.random_elements(elements=products, length=fake.random_int(min=1, max=10), unique=True),
        )
        carts.append(cart)
    return carts

def clear_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    num_fake_users = 10
    num_fake_categories = 5
    num_fake_products = 20
    num_fake_reviews = 30
    num_fake_orders = 15
    num_fake_carts = 10

    clear_database()

    fake_users = generate_fake_users(num_fake_users)
    fake_categories = generate_fake_categories(num_fake_categories)
    fake_products = generate_fake_products(num_fake_products, fake_categories)
    fake_reviews = generate_fake_reviews(num_fake_reviews, fake_users, fake_products)
    fake_orders = generate_fake_orders(num_fake_orders, fake_users, fake_products)
    fake_carts = generate_fake_carts(num_fake_carts, fake_users, fake_products)

    with app.app_context():
        db.create_all()

        db.session.add_all(fake_users)
        db.session.add_all(fake_categories)
        db.session.add_all(fake_products)
        db.session.add_all(fake_reviews)
        db.session.add_all(fake_orders)
        db.session.add_all(fake_carts)

        db.session.commit()

        print('Database seeded successfully!')
