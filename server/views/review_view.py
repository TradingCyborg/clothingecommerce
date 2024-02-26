from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import db, Review, Customer, Product

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/reviews', methods=['POST'])
@jwt_required()
def create_review():
    data = request.json  
    user_id = get_jwt_identity()

    # Extracting data from the request
    rating = data.get('rating')
    comment = data.get('comment')
    date = data.get('date')
    product_id = data.get('product_id')

    # Validate input data
    if not all([rating, comment, date, product_id]):
        return jsonify({'message': 'Incomplete data'}), 400

    try:
        # Validate rating
        if not (0 <= rating <= 6):
            return jsonify({'Please provide a rating between 0 and 6'}), 400

        # Check if the specified product exists
        product = Product.query.get(product_id)

        if not product:
            return jsonify({'Product not found'}), 404

        # Create a new review associated with the logged-in user
        new_review = Review(
            rating=rating,
            comment=comment,
            date=date,
            customer_id=user_id,
            product=product
        )

        # Add the review to the database
        db.session.add(new_review)
        db.session.commit()

        return jsonify({'message': 'Review created successfully'}), 201

    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    user_id = get_jwt_identity()

    try:
        review = Review.query.get(review_id)

        if not review:
            return jsonify({'message': 'Review not found'}), 404

        # Check if the user owns the review
        if review.customer_id != user_id:
            return jsonify({'message': 'Unauthorized to delete this review'}), 403

        db.session.delete(review)
        db.session.commit()

        return jsonify({'message': 'Review deleted successfully'}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    data = request.json
    user_id = get_jwt_identity()

    # Validate input data
    if not data:
        return jsonify({'message': 'No data provided for update'}), 400

    try:
        review = Review.query.get(review_id)

        if not review:
            return jsonify({'message': 'Review not found'}), 404

        # Check if the user owns the review
        if review.customer_id != user_id:
            return jsonify({'message': 'Unauthorized to update this review'}), 403

        # Update review fields
        for key, value in data.items():
            setattr(review, key, value)

        # Validate updated rating
        if 'rating' in data and not (0 <= review.rating <= 6):
            return jsonify({'message': 'Please provide a rating between 0 and 6'}), 400

        db.session.commit()

        return jsonify({'message': 'Review updated successfully'}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500
