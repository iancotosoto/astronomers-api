class Country:

    # Constructor
    def __init__(self, id:str, name:str, continent:str):
        self.id = id #  ISO 3166 Alpha 3 code
        self.name = name
        self.continent = continent

    # Methods
    # Getters
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_continent(self):
        return self.continent
    
    # Setters
    def set_id(self, id:str):
        self.id = id

    def set_name(self, name:str):
        self.name = name
    
    def set_continent(self, id_continent:int):
        self.id_continent = id_continent
        
    # Make a dictionary from the object
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "continent": self.continent
        }