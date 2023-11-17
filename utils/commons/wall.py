from thing import Thing

class wall(Thing):
    
    def __init__(self, literal_name, interactive, collision) -> None:
        super().__init__(self, literal_name, interactive, collision)
        opaque = True
        stackable = False
        container = False