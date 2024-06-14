class Astronomer:

    # Construtor
    def __init__(self, id:int, name:str, birth_year:int, death_year:int, countries:list):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.countries = countries

    # Methods
    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_birth_year(self):
        return self.birth_year
    
    def get_death_year(self):
        return self.death_year
    
    def get_countries(self):
        return self.countries
    
    # Setters
    def set_id(self, id:int):
        self.id = id

    def set_name(self, name:str):
        self.name = name

    def set_birth_year(self, birth_year:int):
        self.birth_year = birth_year
    
    def set_death_year(self, death_year:int):
        self.death_year = death_year
    
    def set_countries(self, countries:list):
        self.countries = countries

    # Make a dictionary from the object
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "death_year": self.death_year,
            "countries": self.countries
        }