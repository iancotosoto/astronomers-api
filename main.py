from flask import Flask

from app.routes.astronomer_routes import astronomer_routes

# Create the Flask app
app = Flask(__name__)

# Register the blueprints
app.register_blueprint(astronomer_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)