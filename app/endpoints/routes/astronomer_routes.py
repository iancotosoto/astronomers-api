from flask import Blueprint

import app.services.astronomer_service as astronomer_service
import data.webscrapping.countries as countries # Delete this line

# Variable to hold the blueprint object
astronomer_routes = Blueprint('astronomer_routes', __name__)

# Routes
@astronomer_routes.route('/test', methods=['GET'])
def test():
    return str(countries.get_countries())

@astronomer_routes.route('/astronomers', methods=['GET'])
def get_astronomers():
    """
    Get all astronomers
    """
    return astronomer_service.get_astronomers()