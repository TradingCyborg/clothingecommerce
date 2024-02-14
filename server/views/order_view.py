from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import Order, db
from sqlalchemy.orm import joinedload

order_bp = Blueprint('order_bp', __name__)

# Fetch all orders
@order_bp.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()

    result = []
    for order in orders:
        result.append({
            'id': order.id,
            'product_id': order.product_id,
            'status': order.status,
            'price': order.price,
            'updated_at': order.updated_at,
            'order_date': order.orderdate.strftime('%Y-%m-%d'),
            'customer': {
                'id': order.customer.id if order.customer else None,
                'username': order.customer.username if order.customer else None
            }
        })

    return jsonify(result), 200

# Fetch a single order
@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    result = []

    if order:
        result.append({
            'id': order.id,
            'product_id': order.product_id,
            'status': order.status,
            'price': order.price,
            'updated_at': order.updated_at,
            'order_date': order.orderdate.strftime('%Y-%m-%d'),
            'customer': {'id': order.customer.id, 'username': order.customer.username}
        })

        return jsonify(result)
    return jsonify({"error": "Order not found!"}), 404

# Delete order
@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
# @jwt_required
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"Success": "Deleted successfully"}), 200
    else:
        return jsonify({"Error": "Order not found"}), 404
    
    

# Update an order
@order_bp.route('/orders/<int:order_id>', methods=['PUT'])

# @jwt_required
def update_order(order_id):
    order = Order.query.get(order_id)

    if order:
        data = request.json

        # Update the status if provided
        if 'status' in data:
            order.status = data['status']

        # Update the quantity if provided
        if 'quantity' in data:
            new_quantity = order.quantity + data['quantity']
            order.quantity = new_quantity

        db.session.commit()

        return jsonify({'Success': 'Order updated successfully'}), 200
    else:
        return jsonify({'Error': 'Order not found'}), 404

# Get orders by user
@order_bp.route('/get_orders_by_user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    orders = Order.query.filter_by(customer_id=user_id).all()

    if orders:
        result = []
        for order in orders:
            result.append({
                'id': order.id,
                'product_id': order.product_id,
                'status': order.status,
                'price': order.price,
                'updated_at': order.updated_at,
                'order_date': order.orderdate.strftime('%Y-%m-%d'),
            })

        return jsonify({'orders': result})
    else:
        return jsonify({"error": "No order found for the given user ID!"}), 404


# Fetch all orders by product
@order_bp.route('/orders/by-product/<int:product_id>', methods=['GET'])
def get_orders_by_product(product_id):
    orders = Order.query.filter_by(product_id=product_id).options(joinedload('customer')).all()

    if orders:
        result = []
        for order in orders:
            result.append({
                'id': order.id,
                'product_id': order.product_id,
                'status': order.status,
                'price': order.price,
                'updated_at': order.updated_at,
                'order_date': order.orderdate.strftime('%Y-%m-%d'),
                'customer': {
                    'id': order.customer.id if order.customer else None,
                    'username': order.customer.username if order.customer else None
                }
            })

        return jsonify({'orders': result})
    else:
        return jsonify({"error": "No orders found for the given product ID!"}), 404