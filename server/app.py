from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import timedelta
from flask_jwt_extended import JWTManager
from models import db  # Import your db instance

# Create the Flask app
app = Flask(__name__)

# Configure the app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "wsddf542455r5rdd55d579j8f6f8yfrd57tru"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

# Initialize SQLAlchemy with the app
db.init_app(app)

# Initialize Migrate with the app and db
migrate = Migrate(app, db)

# Initialize CORS with the app
CORS(app)

# Initialize JWTManager with the app
jwt = JWTManager(app)

# Import and register your blueprints
from views.customer_view import customer_bp
from views.product_view import products_bp 
from views.order_view import order_bp
from views.payment_view import payment_bp
from views.review_view import review_bp
from views.favorite_view import favorite_bp
from views.auth_view import auth_bp

app.register_blueprint(favorite_bp,url_prefix='/https://african-products-e-commerce.onrender.com')
app.register_blueprint(auth_bp,url_prefix='/https://african-products-e-commerce.onrender.com')
app.register_blueprint(review_bp,url_prefix='/https://african-products-e-commerce.onrender.com')
app.register_blueprint(order_bp,url_prefix='/https://african-products-e-commerce.onrender.com')
app.register_blueprint(payment_bp,url_prefix='/https://african-products-e-commerce.onrender.com')
app.register_blueprint(customer_bp,url_prefix='/https://african-products-e-commerce.onrender.com')
app.register_blueprint(products_bp,url_prefix='/https://african-products-e-commerce.onrender.com')

# Run the app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
