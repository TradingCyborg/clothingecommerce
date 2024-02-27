from flask import request, jsonify, Blueprint
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from models import db, Customer, TokenBlocklist

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/token_blocklist', methods=["GET"])
def get_token_blocklist():
    tokens = TokenBlocklist.query.all()
    tokens_list = []
    if tokens:
        for token in tokens:
            tokens_list.append({
                "id": token.id,
                'token': token.token,
                'created_at': token.created_at,
            })
        return jsonify(tokens_list), 200
    else:
        return jsonify({'message': "No tokens found in the blocklist😞"}), 200
    
    
# add customer
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    customer = Customer.query.filter_by(email=email).first()

    if customer:
        stored_password = customer.password
        # Use check_password_hash to verify the hashed password
        if check_password_hash(stored_password, password):
            access_token = create_access_token(identity=customer.id)
            return jsonify(access_token=access_token)

        return jsonify({"error": "Incorrect Password!"}), 401

    else:
        return jsonify({"error": "Customer doesn't exist!"}), 404



# Get logged in customer
@auth_bp.route("/authenticated_customer", methods=["GET"])
@jwt_required()
def authenticated_customer():
    current_customer_id = get_jwt_identity() 
    customer = Customer.query.get(current_customer_id)

    if customer:
        customer_data = {
            'id': customer.id,
            'firstname': customer.firstname,
            'lastname': customer.lastname,
            'email': customer.email,
            'phone': customer.phone,
            'address': customer.address
        }
        return jsonify(customer_data), 200
    else:
        return jsonify({"error": "Oops customer not found!"}), 404


# Logout customer
@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jwt_data = get_jwt()
    jti = jwt_data['jti']

    token_b = TokenBlocklist(jti=jti)
    db.session.add(token_b)
    db.session.commit()

    return jsonify({"success": "Logged out successfully!"}), 200
