from flask import Blueprint, request, jsonify
from server.models import db, Customer, Product, Cart

# Create a Blueprint for cart
cart_bp = Blueprint('cart', __name__)

# Create a route to handle GET requests for retrieving a customer's cart
@cart_bp.route('/carts/<int:customer_id>', methods=['GET'])
def get_cart(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        cart = customer.carts.all()
        if cart:
            return jsonify({'cart': [cart_item.to_dict() for cart_item in cart]}), 200
        else:
            return jsonify({'message': 'Customer does not have any items in the cart'}), 404
    else:
        return jsonify({'message': 'Customer not found'}), 404

# Create a route to handle POST requests for adding a product to a customer's cart
@cart_bp.route('/carts/<int:customer_id>', methods=['POST'])
def add_to_cart(customer_id):
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    cart_item = Cart.query.filter_by(customer_id=customer_id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(quantity=quantity, total_price=product.price * quantity, delivery_address=customer.address, customer_id=customer_id, product_id=product_id)
        db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Product added to cart successfully'}), 201

# Create a route to handle PATCH requests for updating the quantity of a product in a customer's cart
@cart_bp.route('/carts/<int:customer_id>/<int:product_id>', methods=['PATCH'])
def update_cart(customer_id, product_id):
    data = request.get_json()
    quantity = data.get('quantity')
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    cart_item = Cart.query.filter_by(customer_id=customer_id, product_id=product_id).first()
    if cart_item:
        if quantity:
            cart_item.quantity = quantity
        cart_item.total_price = product.price * cart_item.quantity
        db.session.commit()
        return jsonify({'message': 'Cart updated successfully'}), 200
    else:
        return jsonify({'message': 'Product not found in cart'}), 404

# Create a route to handle DELETE requests for removing a product from a customer's cart
@cart_bp.route('/carts/<int:customer_id>/<int:product_id>', methods=['DELETE'])
def remove_from_cart(customer_id, product_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    cart_item = Cart.query.filter_by(customer_id=customer_id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message': 'Product removed from cart successfully'}), 200
    else:
        return jsonify({'message': 'Product not found in cart'}), 404

# Create a route to handle DELETE requests for clearing a customer's cart
@cart_bp.route('/carts/<int:customer_id>', methods=['DELETE'])
def clear_cart(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    customer.carts.delete()
    db.session.commit()
    return jsonify({'message': 'Cart cleared successfully'}), 200
