import app.endpoints.utils.response as resp

import app.cache.astronomer_cache as astronomer_cache
import app.database.astronomer_db as astronomer_db

# Functions
# All astronomers
def post_astronomers():
    """
    Post all astronomers
    """
    try:
        # Check if astronomers were already uploaded
        if astronomer_db.get_astronomers_count() > 0:
            return resp.generate_response("error", "Astronomers already uploaded", None, 409)

        astronomer_db.upload_astronomers() # Upload astronomers to db
        astronomer_cache.delete_astronomers() # Delete astronomers from cache
        
        # Check if astronomers were uploaded successfully
        if astronomer_db.get_astronomers_count() > 0:
            return resp.generate_response("success", "Astronomers uploaded successfully", None, 201)
        return resp.generate_response("error", "No astronomers found to upload", None, 404) # If no astronomers found 
                                                                                            # to upload
        
    except Exception as e:
        return resp.generate_response("error", f"Error uploading astronomers: {e}", None, 500)

def get_astronomers(page=1, limit=10):
    """
    Get paginated astronomers
    """
    try:
        # Calculate offset
        offset = (page - 1) * limit

        # Get paginated astronomers from cache
        astronomers = astronomer_cache.get_astronomers(offset, limit)
        
        if astronomers: 
            # If astronomers is not None, return astronomers from cache
            return resp.generate_response("success", "Astronomers retrieved successfully from cache", astronomers, 200)
        
        # If astronomers is None, get paginated astronomers from db
        astronomers = astronomer_db.get_astronomers(offset, limit)

        if not astronomers: # Astronomers is an empty list
            return resp.generate_response("error", "No astronomers found in database", None, 404)
        
        # Set astronomers in cache
        astronomer_cache.set_astronomers(astronomers, offset, limit)
        
        # Return astronomers from db with success message
        return resp.generate_response("success", "Astronomers retrieved successfully from db", astronomers, 200)
    
    except Exception as e:
        # Return error response if any exception occurs
        return resp.generate_response("error", f"Error retrieving astronomers: {e}", None, 500)

# Astronomers by country
def get_astronomers_by_country(country_name, offset=0, limit=10):
    """
    Get astronomers by country
    """
    try:
        # Get astronomers by country from cache
        astronomers = astronomer_cache.get_astronomers_by_country(country_name, offset, limit)
        
        if astronomers:
            # If astronomers is not None, return astronomers by country from cache
            return resp.generate_response("success", f"Astronomers retrieved successfully by country {country_name} from cache", astronomers, 200)
        
        # If astronomers is None, get astronomers by country from db
        astronomers = astronomer_db.get_astronomers_by_country(country_name, offset, limit)

        if not astronomers: # Astronomers is an empty list
            return resp.generate_response("error", f"No astronomers found by country {country_name} in database", None, 404)
        
        # Set astronomers by country in cache
        astronomer_cache.set_astronomers_by_country(country_name, astronomers, offset, limit)
        
        # Return astronomers by country from db with success message
        return resp.generate_response("success", f"Astronomers retrieved successfully by country {country_name} from db", astronomers, 200)
    
    except Exception as e:
        # Return error response if any exception occurs
        return resp.generate_response("error", f"Error retrieving astronomers by country: {e}", None, 500)