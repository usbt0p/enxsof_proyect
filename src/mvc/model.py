import sys
sys.path.insert(0, '.')

from utiles.commons import *
from src.mvc.subject import Subject
from copy import deepcopy
from utiles.commons.absMovable import AbstractMovable
import json

"""
    Model class.
    This class represents a room in the pyhton project.
"""
class Model(Subject, AbstractMovable):
    def __init__(self, x_size, y_size) -> None:
        super().__init__()
        self.x_size = x_size
        self.y_size = y_size
        self.matrix = self.generate_empty_room()
        self.agents = []
    
    
    def generate_empty_room(self) -> list:
        """
        Generates an empty room.
        Returns: a bidimensional zeros list with the size of the room
        """
        return [[0] * self.x_size for _ in range(self.y_size)]


    def generate_agents(self, *agents) -> None:
        """
        Adds an agent to the room.
        """
        for agent in agents:
            self.agents.append(agent)

    def add_agent(self, agent) -> None:
        """
        Adds an agent to the room.
        """
        self.agents.append(agent)

        self.notifyAll() # TODO esto pa q sirve?

    def populate_room(self, filepath:str) -> list:
        """
        Add decorations to the room.
        The decorations are represented by an id_decoration.
        Returns: a bidimensional list with the decorations added
        """

        config = self.read_grid_config_file(filepath)

        # TODO Posible test de unidad
        '''print(self.y_size == len(config), self.y_size, len(config)) 
        print(self.x_size == len(config[0]), self.x_size, len(config[0]))'''

        assert self.y_size == len(config) and self.x_size == len(config[0]),\
              "Size of the map must be equal to size of the config file's map" 
        
        for y, row in enumerate(config):
            for x, literal in enumerate(row):
                match literal:
                    case "Wall":
                        self.matrix[y][x] = thing.Thing(x, y, literal)
                    case "Sofa" | "Table":
                        self.matrix[y][x] = movable.Movable(x, y, literal)
                    case "Door":
                        self.matrix[y][x] = openable.Openable(x, y, literal)
                    case "Fridge":
                        self.matrix[y][x] = mixed.Mixed(x, y, literal)
                                      
        

    def read_grid_config_file(self, file_path:str) -> dict | None:
        """
        Reads a JSON file and returns the parsed data.

        Parameters:
        - file_path (str): The path to the JSON file.

        Returns:
        - Parsed JSON data (dict): The data read from the JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file {file_path}: {e}")
            return None
        
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
        # TODO cambiar esto: tiene que usar los metodos de movable para moverse!!!
        # Por tanto, tambien tiene que hacer try catch de si se intenta ejecutar sobre un no-movible
        if not self.is_position_occupied(new_position_x, new_position_y):
            new = deepcopy(self.matrix[origin_y][origin_x])
            new.x = new_position_x
            new.y = new_position_y
            self.matrix[new_position_y][new_position_x] = new
            self.matrix[origin_y][origin_x] = 0
        



if __name__ == '__main__':
    import utiles.commons.agent as agent
    room = Model(16, 16)
    
    # Example usage:
    file_path = 'assets/default_16x16_room.json'
    
    room.populate_room(file_path)

    gato = agent.Agent("Gato", 7, 7)
    room.generate_agents(gato)

    print(room.matrix)
    print(room.agents[0])

    room.move_object(7, 4, 1, 1)
    print(room.matrix[1][1])
    