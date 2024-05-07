from flask import Flask

from models import db
from src.controllers.health_data_controller import health_data
from src.controllers.user_controller import user
from src.controllers.login_controller import login
from src.controllers.generate_prompt_controller import query
from utils import config


# Function to handle CORS headers
def add_cors_headers(response):
    # Replace '*' with the origins you want to allow, or use a list of allowed origins
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers[
        'Access-Control-Allow-Credentials'] = 'true'  # Set to 'true' if your API supports credentials (e.g., cookies)
    return response


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    # Register the function as a decorator to be applied to all routes
    app.after_request(add_cors_headers)
    app.register_blueprint(user)
    app.register_blueprint(health_data)
    app.register_blueprint(login)
    app.register_blueprint(query)
    app.run(debug=True)
