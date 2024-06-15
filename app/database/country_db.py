import app.models.country as Country
import app.database.connector as connector
import app.data.get.countries as countries_data

conn = connector.get_db_connection()

def upload_countries():
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

def transform_countries(countries):
    transformed_countries = []
    for country in countries:
        transformed_country = Country.Country(country[0], country[1], country[2])
        transformed_countries.append(transformed_country.to_dict())
    return transformed_countries

def get_countries(offset, limit):
    """
    Get paginated countries from the database
    """
    try:
        cur = conn.cursor()
        cur.execute(f"""
        SELECT C.id, C.name, CT.name FROM Country AS C
        INNER JOIN Continent AS CT ON C.id_continent = CT.id
        LIMIT {limit} OFFSET {offset}
        """)
        countries = cur.fetchall()
        countries = transform_countries(countries)
        cur.close()
        return countries
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
