
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import Customer, db
from sqlalchemy.orm import joinedload

customer_bp = Blueprint('customer_bp', __name__)

# Route for user registration
@customer_bp.route('/signup', methods=['POST'])
def register():
    # Get user data from the request
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    address = data.get('address')

    # Check if the email or phone is already registered
    existing_customer_email = Customer.query.filter_by(email=email).first()
    existing_customer_phone = Customer.query.filter_by(phone=phone).first()
    
    if existing_customer_email:
        return jsonify({'message': 'Email already exists'}), 400

    if existing_customer_phone:
        return jsonify({'message': 'Phone number already exists'}), 400

    # Create a new customer object
    new_customer = Customer(name=name, email=email, phone=phone, password=password, address=address)

    # Add the new customer to the database
    db.session.add(new_customer)
    db.session.commit()

    return jsonify({'message': 'Registration successful'})

# Authenticate user
@customer_bp.route('/login', methods=['POST'])
def login():
    # Get email and password from the request
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Query the database for the customer with the provided email
    customer = Customer.query.filter_by(email=email).first()

    # Check if the customer exists and if the provided password is correct
    if customer and customer.password == password:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid email or password'}), 401