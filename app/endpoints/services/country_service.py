import app.endpoints.utils.response as resp

import app.cache.country_cache as country_cache
import app.database.country_db as country_db

# Functions
# All countries
def post_countries():
    """
    Post all countries
    """
    try:
        # Check if countries were already uploaded
        if country_db.get_countries_count() > 0:
            return resp.generate_response("error", "Countries already uploaded", None, 409)

        country_db.upload_countries()  # Upload countries to db
        country_cache.delete_countries()  # Delete countries from cache
        
        # Check if countries were uploaded successfully
        if country_db.get_countries_count() > 0:
            return resp.generate_response("success", "Countries uploaded successfully", None, 201)
        return resp.generate_response("error", "No countries found to upload", None, 404) # If no countries found
                                                                                            # to upload
        
    except Exception as e:
        return resp.generate_response("error", f"Error uploading countries: {e}", None, 500)

def get_countries(page, limit):
    """
    Get all countries
    """
    try:
        # Calculate offset
        offset = (page - 1) * limit

        # Get countries from cache
        countries = country_cache.get_countries(offset, limit)
        
        if countries:
            # If countries is not None, return countries from cache
            return resp.generate_response("success", "Countries retrieved successfully from cache", countries, 200)
        
        # If countries is None, get countries from db
        countries = country_db.get_countries(offset, limit)

        if not countries: # Countries is an empty list
            return resp.generate_response("success", "No countries found in database", None, 200)
        
        # Set countries in cache
        country_cache.set_countries(countries, offset, limit)
        
        # Return countries from db with success message
        return resp.generate_response("success", "Countries retrieved successfully from db", countries, 200)
    
    except Exception as e:
        # Return error response if any exception occurs
        return resp.generate_response("error", f"Error retrieving countries: {e}", None, 500)