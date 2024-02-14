from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models import db, Favorite

favorite_bp = Blueprint('favorites_bp', __name__)

# Add a favorite item
@favorite_bp.route('/favorites', methods=['POST'])

# @jwt_required
def create_favorite():
    data = request.form
    new_favorite_item = Favorite(
        customer_id=data['customer_id'],
        product_id=data.get('product_id')
    
    )
    db.session.add(new_favorite_item)
    db.session.commit()
    
    return 'New favorite item created successfully!', 201


# Retrieve a favorite item
@favorite_bp.route('/favorites/<int:favorite_id>', methods=['GET'])
def get_favorite_item(favorite_id):
    favorite_item = Favorite.query.get(favorite_id)
    if favorite_item:
        return {
            'id': favorite_item.id,
            'customer_id': favorite_item.customer_id,
            'product_id': favorite_item.product_id
        }
    return 'Favorite item not found', 404

# Remove a favorite item
@favorite_bp.route('/favorites/<int:favorite_id>', methods=['DELETE'])
# @jwt_required
def delete_favorite_item(favorite_id):
    favorite_item = Favorite.query.get(favorite_id)
    if favorite_item:
        db.session.delete(favorite_item)
        db.session.commit()
        return 'Favorite item deleted successfully!', 200
    return 'Favorite item not found', 404





