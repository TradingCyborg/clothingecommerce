from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import timedelta
from flask_jwt_extended import JWTManager
from models import db
from views.product_view import products_bp
from views.order_view import order_bp
from views.review_view import review_bp
from views.cart_view import cart_bp

# Create the Flask app and db object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secrets.token_urlsafe(32)'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

db.init_app(app)

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
