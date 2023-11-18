from utiles.commons.thing import Thing

class Obstacle(Thing):
    
    # TODO mejorar la forma de activar los atributos interactive y colision automaticamente, de forma q no se puedan cambiar 
    def __init__(self, x, y, literal_name, interactive=False, collision=True):
        super().__init__( x, y, literal_name, interactive, collision)

