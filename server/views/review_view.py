from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Review, Customer, Product

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/reviews', methods=['POST'])
# @jwt_required
def create_review():
    data = request.json  

    # Extracting data from the request
    rating = data.get('rating')
    comment = data.get('comment')
    date = data.get('date')
    customer_id = data.get('customer_id')
    product_id = data.get('product_id')

    # Validate input data
    if not all([rating, comment, date, customer_id, product_id]):
        return jsonify({'message': 'Incomplete data'}), 400

    try:
        # Validate rating
        if not (0 <= rating <= 6):
            return jsonify({'Please provide a rating between 0 and 6'}), 400

        # Check if the specified customer and product exist
        customer = Customer.query.get(customer_id)
        product = Product.query.get(product_id)

        if not all([customer, product]):
            return jsonify({'Customer or product not found'}), 404

        # Create a new review
        new_review = Review(
            rating=rating,
            comment=comment,
            date=date,
            customer=customer,
            # product=product
        )

        # Add the review to the database
        db.session.add(new_review)
        db.session.commit()

        return jsonify({'message': 'Review created successfully'}), 201

    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
    
    

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
# @jwt_required
def delete_review(review_id):
    try:
        review = Review.query.get(review_id)

        if not review:
            return jsonify({'message': 'Review not found'}), 404

        db.session.delete(review)
        db.session.commit()

        return jsonify({'message': 'Review deleted successfully'}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
    

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json

    # Validate input data
    if not data:
        return jsonify({'message': 'No data provided for update'}), 400

    try:
        review = Review.query.get(review_id)

        if not review:
            return jsonify({'message': 'Review not found'}), 404

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
