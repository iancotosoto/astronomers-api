\connect astronomy_db;

-- Get all astronomers
CREATE OR REPLACE PROCEDURE get_astronomers() -- NEED TO BE FIXED
LANGUAGE plpgsql
AS $$
DECLARE
    rec RECORD;
    astronomer_id INTEGER;
    astronomer_name TEXT;
    birth_year INTEGER;
    death_year INTEGER;
    country_list TEXT;
BEGIN
    FOR rec IN
        SELECT A.id, A.name, A.birth_year, A.death_year, string_agg(C.name, ', ' ORDER BY C.name) AS countries
        FROM Astronomer A
        LEFT JOIN Astronomer_Country AC ON A.id = AC.astronomer_id
        LEFT JOIN Country C ON AC.country_id = C.id
        GROUP BY A.id, A.name, A.birth_year, A.death_year
        ORDER BY A.name
    LOOP
        astronomer_id := rec.id;
        astronomer_name := rec.name;
        birth_year := rec.birth_year;
        death_year := rec.death_year;
        country_list := rec.countries;

        RAISE NOTICE 'Astronomer ID: %, Name: %, Birth Year: %, Death Year: %, Countries: %',
            astronomer_id, astronomer_name, birth_year, death_year, country_list;
    END LOOP;
END;
$$;

-- Get ids
-- Procedure to get Astronomer ID by name
CREATE OR REPLACE PROCEDURE get_astronomer_id(
    IN p_astronomer_name TEXT,
    OUT p_astronomer_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Search for the Astronomer ID by name
    SELECT id INTO p_astronomer_id FROM Astronomer WHERE name = p_astronomer_name;

    -- If the astronomer is not found, set the ID to NULL
    IF NOT FOUND THEN
        p_astronomer_id := NULL;
        RAISE NOTICE 'Astronomer % not found.', p_astronomer_name;
    END IF;
END;
$$;

-- Inserts
-- Procedure to insert into Astronomer
CREATE OR REPLACE PROCEDURE insert_astronomer(
    IN p_astronomer_name TEXT,
    IN p_birth_year INTEGER,
    IN p_death_year INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Check if the astronomer already exists by name and years
    IF EXISTS (SELECT 1 FROM Astronomer WHERE name = p_astronomer_name AND birth_year = p_birth_year AND death_year = p_death_year) THEN
        RAISE NOTICE 'Astronomer % already exists.', p_astronomer_name;
        RETURN;
    END IF;

    -- Insert the astronomer
    INSERT INTO Astronomer (name, birth_year, death_year) VALUES (p_astronomer_name, p_birth_year, p_death_year);

    -- Commit the transaction
    COMMIT;
END;
$$;

-- Procedure to insert into Astronomer_Country with ID validation
CREATE OR REPLACE PROCEDURE insert_astronomer_country(
    IN p_astronomer_name TEXT,
    IN p_country_name TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_astronomer_id INTEGER;
    v_country_id TEXT;
BEGIN
    -- Get Astronomer ID
    CALL get_astronomer_id(p_astronomer_name, v_astronomer_id);

    -- Get Country ID
    CALL get_country_id(p_country_name, v_country_id);

    -- Check if the relationship Astronomer-Country already exists
    IF EXISTS (SELECT 1 FROM Astronomer_Country WHERE astronomer_id = v_astronomer_id AND country_id = v_country_id) THEN
        RAISE NOTICE 'Astronomer % is already associated with Country %.', p_astronomer_name, p_country_name;
        RETURN;
    END IF;

    -- Insert the Astronomer-Country relationship
    INSERT INTO Astronomer_Country (astronomer_id, country_id) VALUES (v_astronomer_id, v_country_id);

    -- Commit the transaction
    COMMIT;
END;
$$;