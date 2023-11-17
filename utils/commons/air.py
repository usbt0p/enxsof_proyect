from thing import Thing 

class air(Thing):
    
    def __init__(self, literal_name, interactive, collision) -> None:
        super().__init__(self, literal_name, interactive, collision)
        
        opaque = False
        stackable = False
        container = False