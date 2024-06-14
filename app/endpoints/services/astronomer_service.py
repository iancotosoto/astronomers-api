import app.endpoints.utils.response as resp

import cache.astronomer_cache as astronomer_cache
import database.astronomer_db as astronomer_db

def get_astronomers():
    """
    Get all astronomers
    """
    # Get astronomers from cache
    astronomers = astronomer_cache.get_astronomers()
    if astronomers: # If astronomers is not None, return astronomers from cache
        return resp.generate_response("success", "Astronomers retrieved successfully from cache", astronomers, 200)
    else: # If astronomers is None, get astronomers from db
        astronomers = astronomer_db.get_astronomers() # Get astronomers from db
        astronomer_cache.set_astronomers(astronomers) # Set astronomers in cache
        return resp.generate_response("success", "Astronomers retrieved successfully from db", astronomers, 200)
    