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

