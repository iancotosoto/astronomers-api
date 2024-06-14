import app.models.country as Country
import database.db as db
from data.utils.files_managment import read_file
import json

conn = db.get_db_connection()

def upload_countries():
    countries = read_file("./data/files/countries/countries", ".json")
    countries = json.loads(countries)
    countries = countries["countries"]
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

def get_countries():
    try:
        cur = conn.cursor()
        cur.execute("SELECT C.id, C.name, CT.name FROM Country AS C\
                    INNER JOIN Continent AS CT ON C.id_continent = CT.id") # NEED TO BE A PROCEDURE
        countries = cur.fetchall()
        countries = transform_countries(countries)
        cur.close()
        return countries
    except Exception as e:
        print(f"Error getting astronomers: {e}")
        raise e