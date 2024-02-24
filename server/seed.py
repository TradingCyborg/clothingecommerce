<<<<<<< HEAD
from app import app
from models import db, Customer, Profile, Category, Product, Cart, Order, Review
from datetime import datetime

# Create sample data function
def create_sample_data():
    # Add categories
    category1 = Category(name='Shirts')
    category2 = Category(name='Pants')
    db.session.add_all([category1, category2])

    # Add products
    product1 = Product(name='Red T-Shirt', description='A simple red t-shirt', price=19.99, category=category1, imageUrl='https://example.com/image1.jpg', size=1)
    product2 = Product(name='Blue Jeans', description='A pair of blue jeans', price=29.99, category=category2, imageUrl='https://example.com/image2.jpg', size=2)
    db.session.add_all([product1, product2])

    # Add customers
    customer1 = Customer(name='John Doe', email='john@example.com', phone='123456789', password='hashedpassword', address='1234 Main St')
    customer2 = Customer(name='Jane Doe', email='jane@example.com', phone='987654321', password='hashedpassword', address='5678 Elm St')
    db.session.add_all([customer1, customer2])

    # Add carts
    cart1 = Cart(customer=customer1, total_price=49.98, delivery_address='1234 Main St')
    cart2 = Cart(customer=customer2, total_price=29.99, delivery_address='5678 Elm St')
    db.session.add_all([cart1, cart2])

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

if __name__ == '__main__':
    with app.app_context():
        create_sample_data()
        print('Sample data added successfully!')
=======
from app import app, db
from datetime import datetime
from models import Product, Category, Order, Customer, User, Review, product_order_association

def create_sample_data():
    category_names = ['Shirts', 'Pants']
    for name in category_names:
        category = Category.query.filter_by(name=name).first()
        if category is None:
            category = Category(name=name)
            db.session.add(category)

    # Get the categories again to ensure we have the objects with IDs
    categories = Category.query.all()

    product1 = Product(name='Red T-Shirt', description='A simple red t-shirt', price=19.99, category=categories[0], imageUrl='https://example.com/image1.jpg', stock_quantity=10)
    product2 = Product(name='Blue Jeans', description='A pair of blue jeans', price=29.99, category=categories[1], imageUrl='https://example.com/image2.jpg', stock_quantity=20)
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()

    # Create and add sample customers to the database
    customer1 = Customer(name='John Doe', email='john.doe@example.com', phone='123-456-7890', address='123 Main St')
    customer1.password = 'password123'
    customer2 = Customer(name='Jane Doe', email='jane.doe@example.com', phone='123-456-7891', address='456 Elm St')
    customer2.password = 'password123'
    db.session.add(customer1)
    db.session.add(customer2)
    db.session.commit()

    # Create and add sample orders to the database
    order1 = Order(order_date=datetime.now(), total_price=59.98, customer_id=customer1.id)
    order2 = Order(order_date=datetime.now(), total_price=39.98, customer_id=customer2.id)
    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()

    print('Sample data created successfully.')


if __name__ == '__main__':
    with app.app_context():
        create_sample_data()
>>>>>>> 602a5ef (Authentication added)
