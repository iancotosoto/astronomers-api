\connect astronomy_db;

-- Create Continent table
CREATE TABLE IF NOT EXISTS Continent (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create Country table
CREATE TABLE IF NOT EXISTS Country (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    id_continent INTEGER,
    FOREIGN KEY (id_continent) REFERENCES Continent(id)
);