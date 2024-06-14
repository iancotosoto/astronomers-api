import os

class Config:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', 5432)
    DB_NAME = os.getenv('DB_NAME', 'flask_restapi')
    DB_USER = os.getenv('DB_USER', 'flask_restapi')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'flask_restapi_pass')

    CACHE_HOST = os.getenv('CACHE_HOST', 'localhost')
    CACHE_PORT = os.getenv('CACHE_PORT', 6379)
    CACHE_DB = os.getenv('CACHE_DB', 0)
    CACHE_DECODE_RESPONSES = os.getenv('CACHE_DECODE_RESPONSES', True)