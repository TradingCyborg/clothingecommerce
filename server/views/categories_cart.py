from flask import Blueprint, jsonify, request
from server.models import db, Category, Product, Cart
from sqlalchemy.exc import IntegrityError

categories_cart_bp = Blueprint('categories_cart', __name__)

@categories_cart_bp.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    categories_dict = [category.to_dict() for category in categories]
    return jsonify({'categories': categories_dict}), 200

@categories_cart_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    return jsonify({'category': category.to_dict()}), 200

@categories_cart_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'message': 'Name is required'}), 400
    category = Category(name=name)
    db.session.add(category)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Category name must be unique'}), 400
    return jsonify({'category': category.to_dict()}), 201

@categories_cart_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'}), 200

@categories_cart_bp.route('/categories/<int:category_id>/products', methods=['GET'])
def get_products_by_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    products = category.products.all()
    products_dict = [product.to_dict() for product in products]
    return jsonify({'products': products_dict}), 200

@categories_cart_bp.route('/categories/<int:category_id>/products', methods=['POST'])
def create_product_in_category(category_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    imageUrl = data.get('imageUrl')
    size = data.get('size')
    if not name or not description or not price or not imageUrl or not size:
        return jsonify({'message': 'Missing required fields'}), 400
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    product = Product(name=name, description=description, price=price, imageUrl=imageUrl, size=size, category_id=category_id)
    db.session.add(product)
    db.session.commit()
    return jsonify({'product': product.to_dict()}), 201

@categories_cart_bp.route('/categories/<int:category_id>/products/<int:product_id>', methods=['DELETE'])
def delete_product_in_category(category_id, product_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

@categories_cart_bp.route('/categories/<int:category_id>/carts', methods=['GET'])
def get_carts_in_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    products = category.products.all()
    carts = []
    for product in products:
        carts += [cart.to_dict() for cart in product.carts.all()]
    return jsonify({'carts': carts}), 200
