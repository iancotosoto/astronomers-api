from flask import Flask

from src.app.endpoints.routes.astronomer_routes import astronomer_routes
from src.app.endpoints.routes.country_routes import country_routes

# Create the Flask app
app = Flask(__name__, static_url_path='/static')

# Register the blueprints
app.register_blueprint(astronomer_routes)
app.register_blueprint(country_routes)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)