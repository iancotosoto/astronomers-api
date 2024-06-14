\connect astronomy_db;

-- Get ids
-- Procedure to get Continent ID by name
CREATE OR REPLACE PROCEDURE get_continent_id(
    IN p_continent_name TEXT,
    OUT p_continent_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Search for the Continent ID by name
    SELECT id INTO p_continent_id FROM Continent WHERE name = p_continent_name;

    -- If the continent is not found, set the ID to NULL
    IF NOT FOUND THEN
        p_continent_id := NULL;
        RAISE NOTICE 'Continent % not found.', p_continent_name;
    END IF;
END;
$$;

-- Procedure to get Country ID by name
CREATE OR REPLACE PROCEDURE get_country_id(
    IN p_country_name TEXT,
    OUT p_country_id TEXT
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

-- Inserts
-- Procedure to insert into Continent
CREATE OR REPLACE PROCEDURE insert_continent(
    IN p_continent_id INTEGER,
    IN p_continent_name TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Check if the continent already exists by its ID
    IF EXISTS (SELECT 1 FROM Continent WHERE id = p_continent_id) THEN
        RAISE NOTICE 'Continent with ID % already exists.', p_continent_id;
        RETURN;
    END IF;

    -- Insert the continent
    INSERT INTO Continent (id, name) VALUES (p_continent_id, p_continent_name);

    -- Commit the transaction
    COMMIT;
END;
$$;

-- Procedure to insert into Country
CREATE OR REPLACE PROCEDURE insert_country(
    IN p_country_id TEXT,
    IN p_country_name TEXT,
    IN p_id_continent INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Check if the country already exists by its ID
    IF EXISTS (SELECT 1 FROM Country WHERE id = p_country_id) THEN
        RAISE NOTICE 'Country with ID % already exists.', p_country_id;
        RETURN;
    END IF;

    -- Insert the country
    INSERT INTO Country (id, name, id_continent) VALUES (p_country_id, p_country_name, p_id_continent);

    -- Commit the transaction
    COMMIT;
END;
$$;
