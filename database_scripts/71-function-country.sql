\connect astronomy_db;

-- Function to get paginated countries
CREATE OR REPLACE FUNCTION get_paginated_countries(
    p_offset INT,
    p_limit INT
)
RETURNS TABLE (
    id VARCHAR(3),
    name VARCHAR(100),
    continent_name VARCHAR(10)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT C.id, C.name, CT.name AS continent_name
    FROM Country AS C
    INNER JOIN Continent AS CT ON C.id_continent = CT.id
    ORDER BY C.name
    LIMIT p_limit OFFSET p_offset;
END;
$$;