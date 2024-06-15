import json

import app.cache.connector as connector

# Variables
conn = connector.get_cache_connection()

# Functions
# All countries
def set_countries(countries, offset, limit):
    """
    Set countries in the cache
    """
    try:
        conn.setex(f'countries_{offset}_{limit}', 3600, json.dumps(countries)) # Set the key 'countries' with the value of the countries
    except Exception as e: # Handle exceptions
        print(f"Error setting countries in cache: {e}")
        raise e

def get_countries(offset, limit):
    """
    Get all countries from the cache
    """
    try:
        countries = conn.get(f'countries_{offset}_{limit}') # If the key does not exist, it will return None
        return json.loads(countries) if countries else None # Decode the bytes to string
    except Exception as e: # Handle exceptions
        pass

def delete_countries():
    """
    Delete all countries from the cache
    """
    try:
        keys = conn.keys('astronomers_*')
        for key in keys:
            conn.delete(key)
    except Exception as e: # Handle exceptions
        print(f"Error deleting countries from cache: {e}")
        raise e