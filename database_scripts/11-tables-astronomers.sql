\connect astronomy_db;

-- Create Astronomer table
CREATE TABLE IF NOT EXISTS Astronomer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_year INTEGER,
    death_year INTEGER
);

-- Create Astronomer_Country relationship table
CREATE TABLE IF NOT EXISTS Astronomer_Country (
    astronomer_id INTEGER,
    country_id VARCHAR(3),
    PRIMARY KEY (astronomer_id, country_id),
    FOREIGN KEY (astronomer_id) REFERENCES Astronomer(id),
    FOREIGN KEY (country_id) REFERENCES Country(id)
);