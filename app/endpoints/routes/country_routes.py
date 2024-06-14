from flask import Blueprint

import app.services.country_service as country_service

# Variable to hold the blueprint object
country_routes = Blueprint('country_routes', __name__)

# Routes
@country_routes.route('/countries/post', methods=['GET']) # Change endpoint and method
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
    return country_service.get_countries()