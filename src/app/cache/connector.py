import redis

from app.config.config import Config

# Functions
def get_cache_connection():
    """
    Get cache connection
    """
    try:
        conn = redis.Redis(
            host=Config.CACHE_HOST, 
            port=Config.CACHE_PORT, 
            db=Config.CACHE_DB, 
            decode_responses=Config.CACHE_DECODE_RESPONSES
        )
        return conn
    except Exception as e:
        print(f"Error connection to cache: {e}")
        raise e