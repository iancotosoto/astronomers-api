import json

import app.cache.connector as cache

# Variables
conn = cache.get_cache_connection()

# Functions
# All astronomers
def get_astronomers(offset, limit):
    """
    Get paginated astronomers from the cache
    """
    try:
        astronomers = conn.get(f'astronomers_{offset}_{limit}')
        return json.loads(astronomers) if astronomers else None
    except Exception as e:
        print(f"Error getting astronomers from cache: {e}")
        return None

def set_astronomers(astronomers, offset, limit):
    """
    Set paginated astronomers in the cache
    """
    try:
        conn.set(f'astronomers_{offset}_{limit}', json.dumps(astronomers) if astronomers else None)
    except Exception as e:
        print(f"Error setting astronomers in cache: {e}")

def delete_astronomers():
    """
    Delete all astronomers from the cache
    """
    try:
        keys = conn.keys('astronomers_*')
        for key in keys:
            conn.delete(key)
    except Exception as e: 
        print(f"Error deleting astronomers from cache: {e}")
        raise e
    
# Astronomers by country
def get_astronomers_by_country(country_name, offset, limit):
    """
    Get astronomers by country from the cache
    """
    try:
        astronomers = conn.get(f'astronomers_by_country_{country_name}_{offset}_{limit}')
        return json.loads(astronomers) if astronomers else None
    except Exception as e:
        print(f"Error getting astronomers by country from cache: {e}")
        return None
    
def set_astronomers_by_country(country_name, astronomers, offset, limit):
    """
    Set astronomers by country in the cache
    """
    try:
        conn.set(f'astronomers_by_country_{country_name}_{offset}_{limit}', json.dumps(astronomers) if astronomers else None)
    except Exception as e:
        print(f"Error setting astronomers by country in cache: {e}")

def delete_astronomers_by_country():
    """
    Delete astronomers by country from the cache
    """
    try:
        keys = conn.keys(f'astronomers_by_country_*')
        for key in keys:
            conn.delete(key)
    except Exception as e: 
        print(f"Error deleting astronomers by country from cache: {e}")
        raise e