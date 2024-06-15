from flask import Blueprint

import app.endpoints.services.astronomer_service as astronomer_service

# Variable
astronomer_routes = Blueprint('astronomer_routes', __name__)

# Routes
# All astronomers
@astronomer_routes.route('/astronomers', methods=['POST'])
def post_astronomer():
    """
    Post all countries
    """
    return astronomer_service.post_astronomers()

@astronomer_routes.route('/astronomers', methods=['GET'])
def get_astronomers():
    """
    Get all astronomers
    """
    return astronomer_service.get_astronomers()