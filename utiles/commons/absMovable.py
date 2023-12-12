import sys
sys.path.insert(0, '.')

from abc import ABC

class AbstractMovable(ABC):
    """
    Abstract base class for movable objects.
    """

    def move_up(self):
        """
        Move the object up.
        """
        assert self.y > 0, "You can't move there!"
        self.y -= 1


    def move_down(self):
        """
        Move the object down.
        """
        #TODO cambiar esto para cuando esté el mapa
        #assert self.y < len(self.grid) - 1, "You can't move there!"
        self.y += 1

  
    def move_left(self):
        """
        Move the object to the left.
        """
        assert self.x > 0, "You can't move there!"
        self.x -= 1

    
    def move_right(self):
        """
        Move the object to the right.
        """
        #TODO cambiar esto para cuando esté el mapa
        # assert self.x < len(self.grid[0]) - 1, "You can't move there!"
        self.x += 1





