import app.models.country as Country
import app.database.connector as connector
import app.data.get.countries as countries_data

conn = connector.get_db_connection()

def transform_countries(countries):
    """
    Transform countries to a list of dictionaries for the response
    """
    transformed_countries = []
    for country in countries:
        transformed_country = Country.Country(country[0], # id (ISO 3166-1 alpha-3 code)
                                              country[1], # name
                                              country[2] # continent_name
                                              )
        transformed_countries.append(transformed_country.to_dict())
    return transformed_countries

def upload_countries():
    """
    Upload countries to the database
    """
    # Get countries
    countries = countries_data.get_countries()

    for country in countries:
        try:
            cur = conn.cursor()
            cur.execute("CALL insert_country(%s, %s, %s);", 
                        (country["id"], country["name"], country["continent"]))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error uploading countries: {e}")
            conn.rollback()
            raise e

def get_countries(offset, limit):
    """
    Get paginated countries from the database using a user-defined function
    """
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, continent_name FROM get_paginated_countries(%s, %s)", (offset, limit))
        countries = cur.fetchall()
        cur.close()
        t_countries = transform_countries(countries)
        return t_countries
    except Exception as e:
        print(f"Error getting countries: {e}")
        raise e
    
def get_countries_count():
    """
    Returns the count of countries (0 if no countries found).
    """
    try:
        cur = conn.cursor()
        cur.execute("CALL get_countries_count(%s);", (None,))
        result = cur.fetchone()
        cur.close()
        return result[0] if result else 0
    except Exception as e:
        print(f"Error performing query to check countries: {e}")
        return 0  
