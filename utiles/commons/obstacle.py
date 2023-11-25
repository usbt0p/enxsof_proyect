import sys
sys.path.insert(0, '.')

from utiles.commons.thing import Thing

class Obstacle(Thing):
    
    def __init__(self, x, y, literal_name, interactive=False, collision=True):
        super().__init__( x, y, literal_name, interactive, collision)

