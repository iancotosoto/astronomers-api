from flask import Blueprint, request

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
    # Get query parameters
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    return astronomer_service.get_astronomers(page, limit)

# Astronomers by country
@astronomer_routes.route('/astronomers/<country_name>', methods=['GET'])
def get_astronomers_by_country(country_name):
    """
    Get astronomers by country
    """
    # Get query parameters
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    return astronomer_service.get_astronomers_by_country(country_name)