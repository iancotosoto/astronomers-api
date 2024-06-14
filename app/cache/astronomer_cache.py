import cache.cache as cache
import json

# Variable to store the connection to the cache
conn = cache.get_cache_connection()

# Functions to set and get astronomers from the cache
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