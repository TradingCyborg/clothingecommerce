from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import timedelta
from flask_jwt_extended import JWTManager
from models import create_app
from views.product_view import products_bp
from views.order_view import order_bp
from views.review_view import review_bp
from views.cart_view import cart_bp

# Create the Flask app and db object
app, db = create_app()

# Initialize Migrate with the app and db
migrate = Migrate(app, db)

# Initialize CORS with the app
CORS(app)

# Initialize JWTManager with the app
jwt = JWTManager(app)

# Import and register your blueprints
app.register_blueprint(review_bp, url_prefix='/reviews')
app.register_blueprint(order_bp, url_prefix='/orders')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(cart_bp, url_prefix='/cart')

# Run the app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
