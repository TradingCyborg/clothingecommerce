   
from flask import Blueprint, jsonify, request
from models import Customer, db
from flask_jwt_extended import jwt_required



# from flask_jwt_extended import  jwt_required



customer_bp=Blueprint('customerview',__name__)

@customer_bp.route('/customers')
def get_customers():
    """Returns a list of all customers"""
    customers = Customer.query.all()
    customers_list = []
    if customers:
        for customer in customers:
            customers_list.append({
                "id": customer.id,
                'name': customer.name,
                'email': customer.email,
                'phone': customer.phone,
                'address': customer.address,
                'created_at': customer.created_at,
                # Do not return the password in the response
                # 'password': customer.password
            })
        return (customers_list, 200)
    else:
        return jsonify({'message': "No customer found😞"}), 200


@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    if data:
        if 'name' not in data or 'email' not in data or 'phone' not in data or 'password' not in data or 'address' not in data:
            return jsonify({'error': 'All fields are required'}), 400

        name = data['name']
        email = data['email']
        phone = data['phone']
        password = data['password']
        address = data['address']

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        new_customer = Customer(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
            address=address
        )

        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'User created successfully😉'})
    else:
        return jsonify({'error': 'Enter user information❗'})

@customer_bp.route('/customers/<int:id>')
def get_single_customer(id):
    
    customer=Customer.query.filter_by(id=id).first()
    
    if customer:
        return jsonify({
            "id":customer.id,
            'name':customer.name,
            'email':customer.email,
            'phone':customer.phone,
            'address':customer.address,
            'created_at':customer.created_at,
            # Do not return the password in the response
            # 'password': customer.password
        })
    else:
        return jsonify({'message':'User does not exist❗'})


@customer_bp.route('/customers/<int:id>',methods=["PUT",'DELETE','PATCH'])
@jwt_required()
def modify_customer(id):
    customer= Customer.query.filter_by(id=id).first()
    
    if customer:
        
        if request.method == 'DELETE':
            db.session.delete(customer)
            db.session.commit()
            
        elif request.method == 'PATCH':
            data=request.form
            
            customer.name=data.get('name',customer.name)
            customer.email=data.get('email',customer.email)
            customer.phone=data.get('phone',customer.phone)
            customer.address=data.get('address',customer.address)
            # Do not update the password through PATCH request
            # customer.password=data.get('password',customer.password)
            
            db.session.commit()
            return jsonify({"message":"The customer has been updated!"}),201

    else:  
        return jsonify({
            'message':' Customer not found'
    })