from random import choice, randint
import json
from faker import Faker
from app import app
from models import db, Customer, Product
from flask_bcrypt import generate_password_hash
import os

# Get the absolute path to the current script
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)

# Construct the absolute path to db.json
json_path = os.path.join(script_directory, "../client/db.json")

# Open the file using the absolute path
with open(json_path, mode="r") as productdata:
    data = json.load(productdata)

fake = Faker()

with app.app_context():
    Product.query.delete()
    Customer.query.delete()
    db.session.commit()

    customers = []
    passwords = ['ankara', 'black', 'trident', 'beautiful', 'nomatch', 'CTA-125', 'blue']

    for n in range(15):
        # Hash the password using generate_password_hash
        hashed_password = generate_password_hash(f"{choice(passwords)}{randint(3,30)}")
        customer = Customer(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            password=hashed_password
        )
        customers.append(customer)

    db.session.add_all(customers)

    products = []
    for n in data["items"]:
        product = Product(
            name=n["name"],
            price=n["price"],
            description=n["description"],
            category=n["category"],
            quantity=n["stock"],
            imageUrl=n["image_url"]
        )
        products.append(product)

    db.session.add_all(products)
    db.session.commit()
