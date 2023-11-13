import numpy as np

"""
    Room class.
    This class represents a room in the pyhton project.
"""
class Room():
    def __init__(self, room_size):
        self.room_size = room_size
        self.room = self.generate_empty_room()
    
    """
    Generates an empty room.
    Returns: a bidimensional zeros list with the size of the room
    """
    def generate_empty_room(self):
        return np.zeros((self.room_size, self.room_size))
        
    """
    Adds walls and doors to the room.
    The Walls represent the limits of the room.
    One piece of wall is represented by a 1 in the list.
    One piece of door is represented by a 2 in the list.
    Returns: a bidimensional list with the walls added
    """
    def create_room_walls_and_room_doors(self):
        pass

    """
    Add decorations to the room.
    The decorations are represented by an id_decoration.
    Returns: a bidimensional list with the decorations added
    """
    def populate_room(self):
        pass
