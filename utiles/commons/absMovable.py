from abc import ABC, abstractmethod

class AbstractMovable(ABC):
    
    def move_up(self):
        assert self.y > 0, "You can't move there!"
        self.y -= 1

    def move_down(self):
        #TODO cambiar esto para cuando esté el mapa
        #assert self.y < len(self.grid) - 1, "You can't move there!"
        self.y += 1

    def move_left(self):
        assert self.x > 0, "You can't move there!"
        self.x -= 1

    def move_right(self):
        #TODO cambiar esto para cuando esté el mapa
        # assert self.x < len(self.grid[0]) - 1, "You can't move there!"
        self.x += 1



    def generate_random_position(self, max_x, max_y):
        """Generate a random position within the given boundaries."""
        new_x = random.randint(0, max_x - 1)
        new_y = random.randint(0, max_y - 1)
        return new_x, new_y

    def is_valid_position(self, x, y, max_x, max_y):
        """Check if the position is valid (within boundaries and not occupied)."""
        # Check boundaries
        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            return False
        # Check if position is occupied (assuming is_position_occupied is defined)
        return not is_position_occupied(x, y)