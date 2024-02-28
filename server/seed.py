<<<<<<< HEAD
# from app import app
# from models import db, Customer, Profile, Category, Product, Cart, Order, Review, cart_product_association
# from datetime import datetime

# # Create sample data function
# def create_sample_data():
#     # Add categories
#     category_names = ['CASUAL WEAR', 'SPORTS WEAR', 'FORMAL WEAR', 'FOOT WEAR', ]
#     categories = {}

#     for category_name in category_names:
#         existing_category = Category.query.filter_by(name=category_name).first()
#         if existing_category:
#             categories[category_name] = existing_category
#         else:
#             new_category = Category(name=category_name)
#             db.session.add(new_category)
#             categories[category_name] = new_category

#     db.session.commit()

#     # Add products
#     product1 = Product(name='Red T-Shirt', description='A simple red t-shirt', price=19.99, category=categories['CASUAL WEAR'], imageUrl='https://example.com/image1.jpg', size=1)
#     product2 = Product(name='Blue Jeans', description='A pair of blue jeans', price=29.99, category=categories['CASUAL WEAR'], imageUrl='https://example.com/image2.jpg', size=2)
#     db.session.add_all([product1, product2])

#     # Add customers with profiles
#     customer1 = Customer(name='Basil Itumbi', email='basilitumbi@example.com', phone='123456789', password='hashedpassword', address='1234 Main St')
#     profile1 = Profile(bio='Fashion enthusiast', image_url='https://example.com/profile1.jpg', customer=customer1)
#     db.session.add(profile1)

#     customer2 = Customer(name='Jane karari', email='karari@example.com', phone='987654321', password='hashedpassword', address='5678 Elm St')
#     profile2 = Profile(bio='Casual style lover', image_url='https://example.com/profile2.jpg', customer=customer2)
#     db.session.add(profile2)

#     db.session.commit()

#     # Add carts
#     cart1 = Cart(customer=customer1, total_price=49.98, delivery_address='1234 Main St')
#     cart2 = Cart(customer=customer2, total_price=29.99, delivery_address='5678 Elm St')
#     db.session.add_all([cart1, cart2])

#     # Use the association table to associate products with carts
#     cart_product_association.insert().values(cart_id=cart1.id, product_id=product1.id)
#     cart_product_association.insert().values(cart_id=cart1.id, product_id=product2.id)
#     cart_product_association.insert().values(cart_id=cart2.id, product_id=product2.id)

#     # Commit changes
#     db.session.commit()

#     # Add orders
#     order1 = Order(orderdate=datetime.utcnow(), price=49.98, status='pending', customer=customer1, product=product1)
#     order2 = Order(orderdate=datetime.utcnow(), price=29.99, status='pending', customer=customer2, product=product2)
#     db.session.add_all([order1, order2])

#     # Add reviews
#     review1 = Review(rating=4, comment='Good product', date=datetime.utcnow(), customer=customer1, product=product1)
#     review2 = Review(rating=5, comment='Great product', date=datetime.utcnow(), customer=customer2, product=product2)
#     db.session.add_all([review1, review2])

#     # Commit changes
#     db.session.commit()

# if _name_ == '_main_':
#     with app.app_context():
#         create_sample_data()
#         print('Sample data added successfully!')
from app import app
from models import db, Customer, Profile, Category, Product, Cart, Order, Review, cart_product_association
=======

from app import app
from models import db, Customer, UserProfile, Category, Product, Cart, Order, Review, cart_product_association
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca
from datetime import datetime

# Create sample data function
def create_sample_data():
    # Add categories
<<<<<<< HEAD
    category_names = ['CASUAL WEAR', 'SPORTS WEAR', 'FORMAL WEAR', 'FOOT WEAR', ]
    categories = {}

    for category_name in category_names:
        existing_category = Category.query.filter_by(name=category_name).first()
        if existing_category:
            categories[category_name] = existing_category
        else:
            new_category = Category(name=category_name)
            db.session.add(new_category)
            categories[category_name] = new_category

    db.session.commit()

    # Add products
    product1 = Product(name='Red T-Shirt', description='A simple red t-shirt', price=19.99, category=categories['CASUAL WEAR'], imageUrl='https://example.com/image1.jpg', size=1)
    product2 = Product(name='Blue Jeans', description='A pair of blue jeans', price=29.99, category=categories['CASUAL WEAR'], imageUrl='https://example.com/image2.jpg', size=2)
    db.session.add_all([product1, product2])

    # Add customers with profiles
    customer1 = Customer(name='Basil Itumbi', email='basilitumbi@example.com', phone='123456789', password='hashedpassword', address='1234 Main St')
    profile1 = Profile(bio='Fashion enthusiast', image_url='https://example.com/profile1.jpg', customer=customer1)
    db.session.add(profile1)

    customer2 = Customer(name='Jane karari', email='karari@example.com', phone='987654321', password='hashedpassword', address='5678 Elm St')
    profile2 = Profile(bio='Casual style lover', image_url='https://example.com/profile2.jpg', customer=customer2)
=======
    category_names = ['CASUAL WEAR', 'SPORTS WEAR', 'FORMAL WEAR', 'FOOT WEAR']
    categories = {}

    for category_name in category_names:
        existing_category = Category.query.filter_by(name=category_name).first()
        if existing_category:
            categories[category_name] = existing_category
        else:
            new_category = Category(name=category_name)
            db.session.add(new_category)
            categories[category_name] = new_category

    db.session.commit()

    # Add products with placeholder values
    product1 = Product(name='Red T-Shirt', description='A simple red t-shirt', price=19.99, category=categories['CASUAL WEAR'], imageUrl='https://example.com/image1.jpg', size=1)
    product2 = Product(name='Blue Jeans', description='A pair of blue jeans', price=29.99, category=categories['CASUAL WEAR'], imageUrl='https://example.com/image2.jpg', size=2)
    product3 = Product(name='Placeholder Product 1', description='Placeholder description for product 1', price=15.99, category=categories['SPORTS WEAR'], imageUrl='https://example.com/placeholder1.jpg', size=3)
    product4 = Product(name='Placeholder Product 2', description='Placeholder description for product 2', price=24.99, category=categories['FOOT WEAR'], imageUrl='https://example.com/placeholder2.jpg', size=4)
    db.session.add_all([product1, product2, product3, product4])

    # Add customers with profiles
    customer1 = Customer(name='Basil Itumbi', email='basilitumbi@example.com', phone='123456789', password='hashedpassword', address='1234 Main St')
    profile1 = UserProfile(bio='Fashion enthusiast', avatar_url='https://example.com/profile1.jpg', user=customer1)
    db.session.add(profile1)

    customer2 = Customer(name='Jane karari', email='karari@example.com', phone='987654321', password='hashedpassword', address='5678 Elm St')
    profile2 = UserProfile(bio='Casual style lover', avatar_url='https://example.com/profile2.jpg', user=customer2)
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca
    db.session.add(profile2)

    db.session.commit()

    # Add carts
    cart1 = Cart(customer=customer1, total_price=49.98, delivery_address='1234 Main St')
    cart2 = Cart(customer=customer2, total_price=29.99, delivery_address='5678 Elm St')
    db.session.add_all([cart1, cart2])

    # Use the association table to associate products with carts
<<<<<<< HEAD
    cart_product_association.insert().values(cart_id=cart1.id, product_id=product1.id)
    cart_product_association.insert().values(cart_id=cart1.id, product_id=product2.id)
    cart_product_association.insert().values(cart_id=cart2.id, product_id=product2.id)
=======
    db.session.execute(cart_product_association.insert().values(cart_id=cart1.id, product_id=product1.id))
    db.session.execute(cart_product_association.insert().values(cart_id=cart1.id, product_id=product2.id))
    db.session.execute(cart_product_association.insert().values(cart_id=cart2.id, product_id=product2.id))
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca

    # Commit changes
    db.session.commit()

    # Add orders
    order1 = Order(orderdate=datetime.utcnow(), price=49.98, status='pending', customer=customer1, product=product1)
    order2 = Order(orderdate=datetime.utcnow(), price=29.99, status='pending', customer=customer2, product=product2)
    db.session.add_all([order1, order2])

    # Add reviews
    review1 = Review(rating=4, comment='Good product', date=datetime.utcnow(), customer=customer1, product=product1)
    review2 = Review(rating=5, comment='Great product', date=datetime.utcnow(), customer=customer2, product=product2)
    db.session.add_all([review1, review2])

    # Commit changes
    db.session.commit()

if _name_ == '_main_':
    with app.app_context():
        create_sample_data()
<<<<<<< HEAD
        print('Sample data added successfully!')
=======
        print('Sample data added successfully!')
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca
