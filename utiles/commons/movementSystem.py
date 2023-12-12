import sys
sys.path.insert(0, '.')

from abc import ABC
from copy import deepcopy

class Movements(ABC):
    
    def agent_move_up(self):
        assert self.y > 0, "You can't move there!"
        self.y -= 1


    def agent_move_down(self):
        assert self.y < len(self.grid) - 1, "You can't move there!"
        self.y += 1

  
    def agent_move_left(self):
        assert self.x > 0, "You can't move there!"
        self.x -= 1

    
    def agent_move_right(self):
        assert self.x < len(self.grid[0]) - 1, "You can't move there!"
        self.x += 1

    def is_position_occupied(self, x, y) -> bool:
        """
        Checks if a position is occupied by an object.
        Parameters:
        - position (tuple): The position to check.
        Returns:
        - bool: True if the position is occupied, False otherwise.
        """
        return self.matrix[y][x] != 0
    
    def move_object(self, origin_x, origin_y, new_position_x, new_position_y) -> None:
        """
        Moves an object to a new position.
        Parameters:
        - origin (tuple): The position of the object to move.
        - new_position (tuple): The new position of the object.        
        Returns:
        None
        """
        if not self.is_position_occupied(new_position_x, new_position_y):
            new = deepcopy(self.matrix[origin_y][origin_x])
            new.x = new_position_x # Asegura que las coordenadas del objeto se actualizan cuando se mueve
            new.y = new_position_y
            self.matrix[new_position_y][new_position_x] = new
            self.matrix[origin_y][origin_x] = 0
        





