import app.models.astronomer as Astronomer

import database.db as db

conn = db.get_db_connection()

def transform_astronomers(astronomers):
    transformed_astronomers = []
    for astronomer in astronomers:
        transformed_astronomer = Astronomer.Astronomer(
            astronomer[0], astronomer[1], astronomer[2], astronomer[3], astronomer[4].split(", ") 
        )
        transformed_astronomers.append(transformed_astronomer.to_dict())
    return transformed_astronomers

def get_astronomers():
    try:
        cur = conn.cursor()
        cur.execute("SELECT A.id, A.name, A.birth_year, A.death_year, string_agg(C.name, ', ' ORDER BY C.name) AS countries\
        FROM Astronomer A\
        LEFT JOIN Astronomer_Country AC ON A.id = AC.astronomer_id\
        LEFT JOIN Country C ON AC.country_id = C.id\
        GROUP BY A.id, A.name, A.birth_year, A.death_year\
        ORDER BY A.name") # NEED TO BE A PROCEDURE
        astronomers = cur.fetchall()
        astronomers = transform_astronomers(astronomers)
        cur.close()
        return astronomers
    except Exception as e:
        print(f"Error getting astronomers: {e}")
        raise e