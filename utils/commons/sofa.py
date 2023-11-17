from thing import Thing

class sofa(Thing):
        
    def __init__(self, literal_name, interactive, collision) -> None:
        super().__init__(self, literal_name, interactive, collision)
        opaque = True
        stackable = False
        container = True # Lo dejamos en TRUE para que se pueda sentar una persona
        