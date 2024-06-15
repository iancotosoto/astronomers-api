\connect astronomy_db;

-- Create Continent table
CREATE TABLE IF NOT EXISTS Continent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

-- Create Country table
CREATE TABLE IF NOT EXISTS Country (
    id VARCHAR(3) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    id_continent INTEGER,
    FOREIGN KEY (id_continent) REFERENCES Continent(id)
);