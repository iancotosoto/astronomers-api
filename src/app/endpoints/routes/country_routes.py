from flask import Blueprint, request

import app.endpoints.services.country_service as country_service

# Variable to hold the blueprint object
country_routes = Blueprint('country_routes', __name__)

# Routes
# All countries
@country_routes.route('/countries', methods=['POST'])
def post_countries():
    """
    Post all countries
    """
    return country_service.post_countries()

@country_routes.route('/countries', methods=['GET'])
def get_countries():
    """
    Get all countries
    """

    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    return country_service.get_countries(page, limit)
