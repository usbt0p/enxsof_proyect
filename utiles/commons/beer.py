from thing import Thing

class Beer(Thing):
    
    def __init__(self, literal_name, interactive, collision) -> None:
        super().__init__(self, literal_name, interactive, collision)
        opaque = True
        stackable = True
        container = False