# seed.py

from faker import Faker
from models import db, Customer, Profile, Category, Product, Cart, Order, Review, CartProductAssociation
from app import app
from datetime import datetime

fake = Faker()

# Start the application context to make sure db operations are done within it
app.app_context().push()

try:
    # Perform database operations
    # Seed customers
    for _ in range(10):
        customer = Customer(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            password=fake.password(),
            address=fake.address()
        )
        db.session.add(customer)
        profile = Profile(
            bio=fake.sentence(),
            image_url=fake.image_url(),
            customer_id=customer.id
        )
        db.session.add(profile)

    # Commit the changes for customers and profiles
    db.session.commit()
    print("Customers and Profiles seeded successfully!")

except Exception as e:
    print(f"Error occurred during seeding for customers and profiles: {e}")

try:
    # Seed categories
    categories = ["Electronics", "Clothing", "Books", "Toys", "Beauty"]
    for category_name in categories:
        # Check if the category exists
        existing_category = Category.query.filter_by(name=category_name).first()
        if existing_category is None:
            # If it doesn't exist, create it
            category = Category(name=category_name)
            db.session.add(category)

    # Commit the changes for categories
    db.session.commit()
    print("Categories seeded successfully!")

except Exception as e:
    print(f"Error occurred during seeding for categories: {e}")

try:
    # Seed products
    for _ in range(10):
        product = Product(
            name=fake.sentence(nb_words=4),
            description=fake.text(),
            price=fake.random_number(digits=4),
            category_id=fake.random_element(elements=Category.query.all()).id,
            imageUrl=fake.image_url(),
            size=fake.random_number(digits=2)
        )
        db.session.add(product)

    # Commit the changes for products
    db.session.commit()
    print("Products seeded successfully!")

except Exception as e:
    print(f"Error occurred during seeding for products: {e}")

try:
    # Seed reviews
    for _ in range(10):
        review = Review(
            rating=fake.random_number(digits=1),
            comment=fake.sentence(),
            date=fake.date_time_this_year(),
            customer_id=fake.random_element(elements=Customer.query.all()).id,
            product_id=fake.random_element(elements=Product.query.all()).id
        )
        db.session.add(review)

    # Commit the changes for reviews
    db.session.commit()
    print("Reviews seeded successfully!")

except Exception as e:
    print(f"Error occurred during seeding for reviews: {e}")

try:
    # Seed carts
    for customer in Customer.query.all():
        cart = Cart(
            total_price=fake.random_number(digits=5),
            delivery_address=fake.address(),
            customer_id=customer.id
        )
        db.session.add(cart)

        # Add 3 products to each cart
        for _ in range(3):
            cart_product_association = CartProductAssociation(
                cart_id=cart.id,
                product_id=fake.random_element(elements=Product.query.all()).id
            )
            db.session.add(cart_product_association)

    # Commit the changes for carts and cart-product associations
    db.session.commit()
    print("Carts and Cart-product associations seeded successfully!")

except Exception as e:
    print(f"Error occurred during seeding for carts and cart-product associations: {e}")

try:
    # Seed orders
    for _ in range(10):
        order = Order(
            orderdate=fake.date_time_this_year(),
            price=fake.random_number(digits=4),
            status="Shipped",
            customer_id=fake.random_element(elements=Customer.query.all()).id,
            product_id=fake.random_element(elements=Product.query.all()).id
        )
        db.session.add(order)

    # Commit the changes for orders
    db.session.commit()
    print("Orders seeded successfully!")

except Exception as e:
    print(f"Error occurred during seeding for orders: {e}")

