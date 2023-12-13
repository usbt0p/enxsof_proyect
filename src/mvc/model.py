import sys
sys.path.insert(0, '.')

from utiles.commons import *
from src.mvc.subject import Subject
from utiles.commons.movementSystem import Movements, pathPlanning
import json

"""
    Model class.
    This class represents a room in the pyhton project.
"""
class Model(Subject, Movements, pathPlanning):
    def __init__(self, x_size, y_size) -> None:
        """
        Initialize the Model object.

        Args:
            x_size (int): The size of the room in the x-axis.
            y_size (int): The size of the room in the y-axis.
        """
        super().__init__()
        self.x_size = x_size
        self.y_size = y_size
        self.matrix = self.generate_empty_room()
        self.agents = []
    
    
    def generate_empty_room(self) -> list:
        """
        Generates an empty room.
        Returns: a bidimensional list with the size of the room
        """
        return [[0] * self.x_size for _ in range(self.y_size)]


    def generate_agents(self, *agents) -> None:
        """
        Adds an agent to the room.
        """
        for agent in agents:
            self.agents.append(agent)

    def populate_room(self, filepath:str) -> list:
            """
            Populates the room matrix based on the configuration file.

            Args:
                filepath (str): The path to the configuration file.

            Returns:
                list: The populated room matrix.
            """
            config = self.read_grid_config_file(filepath)

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
               




if __name__ == '__main__':
    import utiles.commons.agent as agent
    room = Model(16, 16)
    
    # Example usage:
    file_path = 'assets/default_16x16_room.json'
    
    room.populate_room(file_path)

    gato = agent.Agent("Gato", 7, 7)
    room.generate_agents(gato)

    #print(room.matrix)
    print(room.agents[0])

    print(room.matrix[4][7])
    room.move_object(7, 4, 1, 1)
    print(room.matrix[1][1])
    