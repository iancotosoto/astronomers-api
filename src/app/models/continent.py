class Continent:
    # Constructor
    def __init__(self, id:int, name:str):
        self.id = id 
        self.name = name

    # Methods
    # Getters
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    # Setters
    def set_id(self, id:str):
        self.id = id

    def set_name(self, name:str):
        self.name = name