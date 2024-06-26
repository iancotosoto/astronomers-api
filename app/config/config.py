import os

# Class to store the environment variables
class Config:

    # Database
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    # Cache
    CACHE_HOST = os.getenv('CACHE_HOST')
    CACHE_PORT = os.getenv('CACHE_PORT')
    CACHE_DB = os.getenv('CACHE_DB')
    CACHE_DECODE_RESPONSES = os.getenv('CACHE_DECODE_RESPONSES')

    # Sources (links)
    COUNTRIES_SOURCE = os.getenv('COUNTRIES_SOURCE')
    ASTRONOMERS_SOURCE = os.getenv('ASTRONOMERS_SOURCE')