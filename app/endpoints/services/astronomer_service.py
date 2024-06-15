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

def get_astronomers():
    """
    Get all astronomers
    """
    try:
        # Get astronomers from cache
        astronomers = astronomer_cache.get_astronomers()
        
        if astronomers: 
            # If astronomers is not None, return astronomers from cache
            return resp.generate_response("success", "Astronomers retrieved successfully from cache", astronomers, 200)
        
        # If astronomers is None, get astronomers from db
        astronomers = astronomer_db.get_astronomers()

        if not astronomers: # Astronomers is an empty list
            return resp.generate_response("success", "No astronomers found in database", None, 200)
        
        # Set astronomers in cache
        astronomer_cache.set_astronomers(astronomers)
        
        # Return astronomers from db with success message
        return resp.generate_response("success", "Astronomers retrieved successfully from db", astronomers, 200)
    
    except Exception as e:
        # Return error response if any exception occurs
        return resp.generate_response("error", f"Error retrieving astronomers: {e}", None, 500)
    