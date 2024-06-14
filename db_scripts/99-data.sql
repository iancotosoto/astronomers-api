\connect astronomy_db;

-- Insert Continents
CALL insert_continent(1, 'America');    -- Continent ID 1
CALL insert_continent(2, 'Europe');     -- Continent ID 2
CALL insert_continent(3, 'Asia');       -- Continent ID 3
CALL insert_continent(4, 'Africa');     -- Continent ID 4
CALL insert_continent(5, 'Oceania');    -- Continent ID 5

-- Insert Countries and Associate with Continents
CALL insert_country('USA', 'United States', 1);        -- America
CALL insert_country('CAN', 'Canada', 1);               -- America
CALL insert_country('MEX', 'Mexico', 1);               -- America
CALL insert_country('BRA', 'Brazil', 1);               -- America
CALL insert_country('ARG', 'Argentina', 1);            -- America
CALL insert_country('FRA', 'France', 2);               -- Europe
CALL insert_country('GER', 'Germany', 2);              -- Europe
CALL insert_country('ITA', 'Italy', 2);                -- Europe
CALL insert_country('RUS', 'Russia', 3);               -- Asia
CALL insert_country('CHN', 'China', 3);                -- Asia
CALL insert_country('IND', 'India', 3);                -- Asia
CALL insert_country('SA', 'South Africa', 4);          -- Africa
CALL insert_country('EGY', 'Egypt', 4);                -- Africa
CALL insert_country('NGR', 'Nigeria', 4);              -- Africa
CALL insert_country('AUS', 'Australia', 5);            -- Oceania
CALL insert_country('NZL', 'New Zealand', 5);          -- Oceania
CALL insert_country('FIJ', 'Fiji', 5);                 -- Oceania

-- Insert Astronomers
CALL insert_astronomer('Carl Sagan', 1934, 1996);
CALL insert_astronomer('Galileo Galilei', 1564, 1642);
CALL insert_astronomer('Isaac Newton', 1643, 1727);
CALL insert_astronomer('Albert Einstein', 1879, 1955);
CALL insert_astronomer('Stephen Hawking', 1942, 2018);
CALL insert_astronomer('Edwin Hubble', 1889, 1953);
CALL insert_astronomer('Johannes Kepler', 1571, 1630);
CALL insert_astronomer('Nicolaus Copernicus', 1473, 1543);
CALL insert_astronomer('Neil Armstrong', 1930, 2012);
CALL insert_astronomer('Edmond Halley', 1656, 1742);

-- Connect Astronomers with Countries
CALL insert_astronomer_country('Carl Sagan', 'Canada');
CALL insert_astronomer_country('Carl Sagan', 'Egypt');
CALL insert_astronomer_country('Galileo Galilei', 'Canada');
CALL insert_astronomer_country('Isaac Newton', 'Egypt');
CALL insert_astronomer_country('Albert Einstein', 'Egypt');
CALL insert_astronomer_country('Stephen Hawking', 'Egypt');
CALL insert_astronomer_country('Edwin Hubble', 'India');
CALL insert_astronomer_country('Johannes Kepler', 'India');
CALL insert_astronomer_country('Nicolaus Copernicus', 'Fiji');
CALL insert_astronomer_country('Neil Armstrong', 'China');
CALL insert_astronomer_country('Edmond Halley', 'China');