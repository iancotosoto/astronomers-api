import app.utils.response as resp

import cache.country_cache as country_cache
import database.country_db as country_db

def post_countries():
    """
    Post all countries
    """
    try:
        country_db.upload_countries() # Upload countries to db
        return resp.generate_response("success", "Countries uploaded successfully", None, 200)
    except Exception as e:
        return resp.generate_response("error", f"Error uploading countries: {e}", None, 500)

def get_countries():
    """
    Get all get_countries
    """
    # Get countries from cache
    countries = country_cache.get_countries()
    if countries: # If countries is not None, return countries from cache
        return resp.generate_response("success", "Countries retrieved successfully from cache", countries, 200)
    else: # If countries is None, get countries from db
        countries = country_db.get_countries() # Get countries from db
        country_cache.set_countries(countries) # Set countries in cache
        return resp.generate_response("success", "Countries retrieved successfully from db", countries, 200)