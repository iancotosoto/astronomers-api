\connect astronomy_db;

-- Get
-- Procedure to get Country ID by name
CREATE OR REPLACE PROCEDURE get_country_id(
    IN p_country_name VARCHAR(100),
    OUT p_country_id VARCHAR(3)
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Search for the Country ID by name
    SELECT id INTO p_country_id FROM Country WHERE name = p_country_name;

    -- If the country is not found, set the ID to NULL
    IF NOT FOUND THEN
        p_country_id := NULL;
        RAISE NOTICE 'Country % not found.', p_country_name;
    END IF;
END;
$$;

-- Procedure to get the count of countries
CREATE OR REPLACE PROCEDURE get_countries_count(
    OUT p_country_count INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Perform the query to count the number of countries
    SELECT COUNT(id) INTO p_country_count FROM Country;
END;
$$;

-- Inserts
-- Procedure to insert into Country with continent name
CREATE OR REPLACE PROCEDURE insert_country(
    IN p_country_id VARCHAR,
    IN p_country_name VARCHAR(100),
    IN p_continent_name VARCHAR(100)
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_continent_id INTEGER;
BEGIN
    -- Get the continent ID by name
    CALL get_continent_id(p_continent_name, v_continent_id);

    -- If continent ID is NULL, raise an exception
    IF v_continent_id IS NULL THEN
        RAISE EXCEPTION 'Continent % not found.', p_continent_name;
    END IF;

    -- Check if the country already exists by its ID
    IF EXISTS (SELECT 1 FROM Country WHERE id = p_country_id) THEN
        RAISE NOTICE 'Country with ID % already exists.', p_country_id;
        RETURN;
    END IF;

    -- Insert the country
    INSERT INTO Country (id, name, id_continent) VALUES (p_country_id, p_country_name, v_continent_id);
END;
$$;