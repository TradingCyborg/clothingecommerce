from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate   

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fentywear.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)



from models import User, UserProfile, Category, Product, Review, Order, Cart
# JWT Configuration
def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    except Exception as e:
        return e

def decode_auth_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token has expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

# CRUD Operations for Products

# View all products
@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify({'products': [product.serialize() for product in products]})

# Search for products
@app.route('/products/search', methods=['GET'])
def search_products():
    keyword = request.args.get('keyword')
    products = Product.query.filter(Product.name.ilike(f"%{keyword}%")).all()
    return jsonify({'products': [product.serialize() for product in products]})

# View products based on category
@app.route('/products/category/<category_id>', methods=['GET'])
def get_products_by_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    products = Product.query.filter_by(category_id=category.id).all()
    return jsonify({'products': [product.serialize() for product in products]})

# CRUD Operations for Cart

# View user's cart
@app.route('/cart', methods=['GET'])
def get_user_cart():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Authentication token is missing'}), 401

    auth_token = auth_header.split(" ")[1]
    user_id = decode_auth_token(auth_token)
    
    if not isinstance(user_id, int):
        return jsonify({'error': user_id}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    cart_items = user.cart.products
    return jsonify({'cart': [item.serialize() for item in cart_items]})

# Add product to cart
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Authentication token is missing'}), 401

    auth_token = auth_header.split(" ")[1]
    user_id = decode_auth_token(auth_token)

    if not isinstance(user_id, int):
        return jsonify({'error': user_id}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    product_id = data.get('product_id')
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    user.cart.products.append(product)
    db.session.commit()
    return jsonify({'message': 'Product added to cart successfully'})

# Delete product from cart
@app.route('/cart/delete', methods=['DELETE'])
def delete_from_cart():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Authentication token is missing'}), 401

    auth_token = auth_header.split(" ")[1]
    user_id = decode_auth_token(auth_token)

    if not isinstance(user_id, int):
        return jsonify({'error': user_id}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    product_id = data.get('product_id')
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    user.cart.products.remove(product)
    db.session.commit()
    return jsonify({'message': 'Product removed from cart successfully'})

# CRUD Operations for Reviews

# Add review for a product
@app.route('/reviews/add', methods=['POST'])
def add_review():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Authentication token is missing'}), 401

    auth_token = auth_header.split(" ")[1]
    user_id = decode_auth_token(auth_token)

    if not isinstance(user_id, int):
        return jsonify({'error': user_id}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    product_id = data.get('product_id')
    rating = data.get('rating')
    comment = data.get('comment')

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    new_review = Review(rating=rating, comment=comment, user=user, product=product)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully'})

# Read reviews for a product
@app.route('/reviews/<product_id>', methods=['GET'])
def get_product_reviews(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    reviews = product.reviews
    return jsonify({'reviews': [review.serialize() for review in reviews]})

# Other CRUD operations can be added as needed...

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tables created successfully!")  # Add this line
    app.run(debug=True)
