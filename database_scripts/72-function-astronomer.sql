\connect astronomy_db;


-- Function to get paginated astronomers
CREATE OR REPLACE FUNCTION get_paginated_astronomers(
    p_offset INT,
    p_limit INT
)
RETURNS TABLE (
    id INTEGER,
    name VARCHAR(100),
    birth_year INTEGER,
    death_year INTEGER,
    countries TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT A.id, A.name, A.birth_year, A.death_year, string_agg(C.name, ', ' ORDER BY C.name) AS countries
    FROM Astronomer A
    LEFT JOIN Astronomer_Country AC ON A.id = AC.astronomer_id
    LEFT JOIN Country C ON AC.country_id = C.id
    GROUP BY A.id, A.name, A.birth_year, A.death_year
    ORDER BY A.name
    LIMIT p_limit OFFSET p_offset;
END;
$$;