import cache.cache as cache
import json

# Variable to store the connection to the cache
conn = cache.get_cache_connection()

# Functions to set and get countries from the cache
# All countries
def set_countries(countries):
    """
    Set countries in the cache
    """
    try:
        countries = json.dumps(countries) # Convert the countries to a JSON string
        conn.setex('countries', 3600, countries) # Set the key 'countries' with the value of the countries
    except Exception as e: # Handle exceptions
        print(f"Error setting countries in cache: {e}")
        raise e

def get_countries():
    """
    Get all countries from the cache
    """
    try:
        countries = conn.get('countries') # If the key does not exist, it will return None
        return json.loads(countries) if countries else None # Decode the bytes to string
    except Exception as e: # Handle exceptions
        pass