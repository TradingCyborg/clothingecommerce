# Import necessary modules
from app import db
from models import Category, Product, Customer, Profile, Cart, Order, Review
from sqlalchemy import func

<<<<<<< HEAD
# Function to create sample data
def create_sample_data():
    try:
        # Print a message indicating that categories are being added
        print("Adding categories...")
        # Create a list of category names
        category_names = ['CASUAL WEAR', 'SPORTS WEAR', 'FORMAL WEAR', 'FOOT WEAR']
        # Create a dictionary to store categories
        categories = {}
        # Loop through each category name
        for category_name in category_names:
            # Query the database to check if the category already exists
            existing_category = Category.query.filter(func.lower(Category.name) == func.lower(category_name)).first()
            # If the category already exists, add it to the dictionary
            if existing_category:
                categories[category_name] = existing_category
            # If the category does not exist, create a new category and add it to the database and the dictionary
            else:
                new_category = Category(name=category_name)
                db.session.add(new_category)
                categories[category_name] = new_category
        # Commit the changes to the database
        db.session.commit()
        # Print a message indicating that categories were added successfully
        print("Categories added successfully!")

        # Print a message indicating that products are being added
        print("Adding products...")
        # Loop through each category name and category
        for category_name, category in categories.items():
            # If the category is CASUAL WEAR, create a list of products and add them to the database
            if category_name == 'CASUAL WEAR':
                products = [
                    Product(name='Red T-Shirt', description='A simple red t-shirt', price=1999, category_id=category.id, imageUrl='https://th.bing.com/th/id/OIP.7n5TOdEGuHQrmQA-DC88PQHaLW?w=736&h=1128&rs=1&pid=ImgDetMain', size=1),
                    Product(name='Blue Jeans', description='A pair of blue jeans', price=2999, category_id=category.id, imageUrl='https://th.bing.com/th/id/OIP.VLUh08_Gc30ObixQgf6lbQHaJ4?w=1080&h=1440&rs=1&pid=ImgDetMain', size=2)
                ]
            # If the category is FORMAL WEAR, create a list of products and add them to the database
            elif category_name == 'FORMAL WEAR':
                products = [
                    Product(name='Dress', description='Elegent dress for formal events', price=3999, category_id=category.id, imageUrl='https://th.bing.com/th/id/R.4fc853a0ba16699313a93391c7416f4b?rik=uHMVensdv7JncA&riu=http%3a%2f%2fdzasv7x7a867v.cloudfront.net%2fproduct_photos%2f46820830%2fQQ_E5_9B_BE_E7_89_8720161226102324_original.jpg&ehk=%2bRgXk1t0Bx%2baR%2fRwo%2b9e21H%2fcovKeGvnFMG8RmOAOSU%3d&risl=&pid=ImgRaw&r=0', size=6),
                    Product(name='Skirt', description='This skirt can be paired with any dark colored of your choice', price=2000, category_id=category.id, imageUrl='https://ae01.alicdn.com/kf/HTB117FxXIrrK1RjSspaq6AREXXav/Skirt-Women-Fashion-Solid-Flared-Retro-Casual-Knee-Length-Pleated-Midi-Office-Work-Skirt-Gonna-femminile.jpg', size=1),
                    Product(name='skirt', description='casual stylish skirt', price=1500, category_id=category.id, imageUrl='https://i.pinimg.com/originals/80/ab/12/80ab12f6767e629e444a17ab50fbffcb.png', size=6),
                    Product(name='Trouser', description='This trouser can be paired with any dark colored of your choice', price=2000, category_id=category.id, imageUrl='https://images2.drct2u.com/pdp_main_desktop_x2/products/lf/lf458/m01lf458500w.jpg', size=8)
                ]
            # If the category is not CASUAL WEAR or FORMAL WEAR, create an empty list of products
            else:
                products = []
            # Add the products to the database
            db.session.add_all(products)
            # Commit the changes to the database
            db.session.commit()
            # Print a message indicating that products for the category were added successfully
            print("Products for category '{}' added successfully".format(category_name))

        # Print a message indicating that profiles are being added
        print("Adding profiles...")
        # Create a list of customers
        customers = [
            Customer(name='Basil Itumbi', email='basilitumbi@example.com', phone='123456789', password='hashedpassword', address='1234 Main St'),
            Customer(name='Jane Doe', email='janedoe@example.com', phone='987654321', password='hashedpassword', address='5678 Elm St'),
            Customer(name='John Smith', email='johnsmith@example.com', phone='111223344', password='hashedpassword', address='789 Broadway St'),
            Customer(name='Alice Johnson', email='alicejohnson@example.com', phone='555666777', password='hashedpassword', address='456 Pine St')
        ]
        # Loop through each customer
        for customer in customers:
            # Add the customer to the database
            db.session.add(customer)
            # Commit the changes to the database
            db.session.commit()
            # Create a profile for the customer
            profile = Profile(bio='', image_url='', customer_id=customer.id)
            # Add the profile to the database
            db.session.add(profile)
            # Commit the changes to the database
            db.session.commit()
            # Print a message indicating that the profile was added successfully
            print("Profile for customer '{}' added successfully".format(customer.name))

        # Print a message indicating that carts are being added
        print("Adding carts...")
        # Create a list of carts
        carts = [
            Cart(customer=customers[0], total_price=49.98, delivery_address='1234 Main St'),
            Cart(customer=customers[1], total_price=29.99, delivery_address='5678 Elm St')
        ]
        # Loop through each cart
        for cart in carts:
            # Add the cart to the database
            db.session.add(cart)
            # Commit the changes
            db.session.commit()

    except Exception as e:
        # Rollback changes if an exception occurs
        db.session.rollback()
        # Print the error message
        print(f"Error: {str(e)}")
=======
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
from datetime import datetime
from sqlalchemy import func

# Create sample data function
def create_sample_data():
    print("Adding categories...")
    
    # Add categories
    category_names = ['CASUAL WEAR', 'SPORTS WEAR', 'FORMAL WEAR', 'FOOT WEAR']
    categories = {}

    for category_name in category_names:
        existing_category = Category.query.filter(func.lower(Category.name) == func.lower(category_name)).first()
        if existing_category:
            categories[category_name] = existing_category
        else:
            new_category = Category(name=category_name)
            db.session.add(new_category)
            categories[category_name] = new_category

    db.session.commit()
    print("Categories added successfully!")

    # Add products
    print("Adding products...")
    product1 = Product(
        name='Red T-Shirt',
        description='A simple red t-shirt',
        price=1999,
        category_id=categories['CASUAL WEAR'].id,
        imageUrl='https://th.bing.com/th/id/OIP.7n5TOdEGuHQrmQA-DC88PQHaLW?w=736&h=1128&rs=1&pid=ImgDetMain',
        size=1
    )
    product2 = Product(
        name='Blue Jeans',
        description='A pair of blue jeans',
        price=2999,
        category_id=categories['CASUAL WEAR'].id,
        imageUrl='https://th.bing.com/th/id/OIP.VLUh08_Gc30ObixQgf6lbQHaJ4?w=1080&h=1440&rs=1&pid=ImgDetMain',
        size=2
    )
    product3 = Product(
        name='Dress',
        description='Elegent dress for formal events',
        price=3999,
        category_id=categories['FORMAL WEAR'].id,
        imageUrl='https://th.bing.com/th/id/R.4fc853a0ba16699313a93391c7416f4b?rik=uHMVensdv7JncA&riu=http%3a%2f%2fdzasv7x7a867v.cloudfront.net%2fproduct_photos%2f46820830%2fQQ_E5_9B_BE_E7_89_8720161226102324_original.jpg&ehk=%2bRgXk1t0Bx%2baR%2fRwo%2b9e21H%2fcovKeGvnFMG8RmOAOSU%3d&risl=&pid=ImgRaw&r=0',
        size=6
    )
    product4 = Product(
        name='Skirt',
        description='This skirt can be paired with any dark colored of your choice',
        price=2000,
        category_id=categories['FORMAL WEAR'].id,
        imageUrl='https://ae01.alicdn.com/kf/HTB117FxXIrrK1RjSspaq6AREXXav/Skirt-Women-Fashion-Solid-Flared-Retro-Casual-Knee-Length-Pleated-Midi-Office-Work-Skirt-Gonna-femminile.jpg',
        size=1
    )
    product5 = Product(
        name='skirt',
        description='casual stylish skirt',
        price=1500,
        category_id=categories['FORMAL WEAR'].id,
        imageUrl='https://i.pinimg.com/originals/80/ab/12/80ab12f6767e629e444a17ab50fbffcb.png',
        size=6
    )
    product6 = Product(
        name='Trouser',
        description='This trouser can be paired with any dark colored of your choice',
        price=2000,
        category_id=categories['FORMAL WEAR'].id,
        imageUrl='https://images2.drct2u.com/pdp_main_desktop_x2/products/lf/lf458/m01lf458500w.jpg',
        size=8
    )
    
    db.session.add_all([product1, product2])
    print("Products added successfully")

    # Add profiles
    print("Adding profiles...")
    customer1 = Customer(name='Basil Itumbi', email='basilitumbi@example.com', phone='123456789', password='hashedpassword', address='1234 Main St')
    profile1 = Profile(bio='Fashion enthusiast', image_url='https://example.com/profile1.jpg', customer_id=customer1.id)
    db.session.add(profile1)
    print("Profile for Basil Itumbi created successfully")

    # Add three more customers with profiles
    customer2 = Customer(name='Jane Doe', email='janedoe@example.com', phone='987654321', password='hashedpassword', address='5678 Elm St')
    profile2 = Profile(bio='Fitness lover', image_url='https://example.com/profile2.jpg', customer_id=customer2.id)
    db.session.add(profile2)
    print("Profile for Jane Doe created successfully")

    customer3 = Customer(name='John Smith', email='johnsmith@example.com', phone='111223344', password='hashedpassword', address='789 Broadway St')
    profile3 = Profile(bio='Tech enthusiast', image_url='https://example.com/profile3.jpg', customer_id=customer3.id)
    db.session.add(profile3)
    print("Profile for John Smith created successfully")

    customer4 = Customer(name='Alice Johnson', email='alicejohnson@example.com', phone='555666777', password='hashedpassword', address='456 Pine St')
    profile4 = Profile(bio='Art lover', image_url='https://example.com/profile4.jpg', customer_id=customer4.id)
    db.session.add(profile4)
    print("Profile for Alice Johnson created successfully")

    db.session.commit()
    print("Profiles added successfully")

    # Add carts
    print("Adding carts...")
    cart1 = Cart(customer=customer1, total_price=49.98, delivery_address='1234 Main St')
    cart2 = Cart(customer=customer2, total_price=29.99, delivery_address='5678 Elm St')
    db.session.add_all([cart1, cart2])

    # Use the association table to associate products with carts
    cart_product_association.insert().values(cart_id=cart1.id, product_id=product1.id)
    cart_product_association.insert().values(cart_id=cart1.id, product_id=product2.id)
    cart_product_association.insert().values(cart_id=cart2.id, product_id=product2.id)

    # Commit changes
    db.session.commit()

    # Add orders
    print("Adding orders...")
    order1 = Order(orderdate=datetime.utcnow(), price=49.98, status='pending', customer=customer1, product=product1)
    order2 = Order(orderdate=datetime.utcnow(), price=29.99, status='pending', customer=customer2, product=product2)
    db.session.add_all([order1, order2])
    print("Orders added successfully")

    # Add reviews
    print("Adding reviews...")
    review1 = Review(rating=4, comment='Good product', date=datetime.utcnow(), customer=customer1, product=product1)
    review2 = Review(rating=5, comment='Great product', date=datetime.utcnow(), customer=customer2, product=product2)
    db.session.add_all([review1, review2])

    # Commit changes
    db.session.commit()
    print("Reviews added successfully")


if __name__ == '__main__':
    with app.app_context():
        create_sample_data()
        print('Sample data added successfully!')
>>>>>>> origin/lee-kibugi
