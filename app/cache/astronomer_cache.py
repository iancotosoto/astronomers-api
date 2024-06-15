import json

import app.cache.connector as cache

# Variables
conn = cache.get_cache_connection()

# Functions
# All astronomers
def set_astronomers(astronomers):
    """
    Set astronomers in the cache
    """
    try:
        astronomers = json.dumps(astronomers) # Convert the astronomers to a JSON string
        conn.setex('astronomers', 3600, astronomers) # Set the key 'astronomers' with the value of the astronomers
    except Exception as e: # Handle exceptions
        print(f"Error setting astronomers in cache: {e}")
        raise e

def get_astronomers():
    """
    Get all astronomers from the cache
    """
    try:
        astronomers = conn.get('astronomers') # If the key does not exist, it will return None
        return json.loads(astronomers) if astronomers else None # Decode the bytes to string
    except Exception as e: # Handle exceptions
        pass

def delete_astronomers():
    """
    Delete all astronomers from the cache
    """
    try:
        conn.delete('astronomers') # Delete the key 'astronomers'
    except Exception as e: # Handle exceptions
        print(f"Error deleting astronomers from cache: {e}")
        raise e