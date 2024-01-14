import json
from utiles.commons.movementSystem import Movements, pathPlanning
from src.mvc.subject import Subject
from utiles.objects import (thing, openable, movable, mixed)
from utiles.agents import (agent, nurse, owner)
import sys
sys.path.insert(0, '.')


class Model(Subject, Movements, pathPlanning):
    """
    Model class.
    This class represents a room in the pyhton project.
    """

    def __init__(self, x_size:int, y_size:int) -> None:
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
    
    def create_agent(self, name, x, y):
        """
        Creates an agent in the room.
        """
        return agent.Agent(name, x, y) # TODO hacer el creador bien !!!!!!!

    def create_object(self, x, y, literal):
        """
        Creates an object in the room.
        """
        obj = 0
        match literal:
            case "Wall" | "Juego" | "Juego_g":
                obj = thing.Thing(x, y, literal)
            case "Sofa" | "Table" | "Cama" | "Cama_g" | "Planta1" | "Planta2" | "Planta3" | \
                "Silla_Oficina" | "Silla_Oficina_g" | "Silla1_g" | "Silla1" | "Silla2_g" | "Silla2" | \
                "Vater1":
                obj = movable.Movable(x, y, literal)
            case "Door" | "Door_main":
                obj = openable.Openable(x, y, literal)
            case "Fridge" | "Armario":
                obj = mixed.Mixed(x, y, literal)
            case 2:
                obj = 2
        
        return obj

    def generate_agents(self, *agents) -> None:
        """
        Adds an agent to the room.
        """
        for agent in agents:
            self.agents.append(agent)

    def populate_room(self, filepath: str) -> list:
        """
        Populates the room matrix based on the configuration file.

        Args:
            filepath (str): The path to the configuration file.

        Returns:
            list: The populated room matrix.
        """
        config = self.read_grid_config_file(filepath)

        assert self.y_size == len(config) and self.x_size == len(config[0]), \
            "Size of the map must be equal to size of the config file's map"

        for y, row in enumerate(config):
            for x, literal in enumerate(row):
                self.matrix[y][x] = self.create_object(x, y, literal)

    def read_grid_config_file(self, file_path: str) -> dict | None:
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

    def agents_random_spawn(self, *agents) -> None:
        """
        Spawns the agents in a random position in the room.

        Args:
            agents (list): A list of agents to spawn. The agents must
            be instantiated, but their coordinates will change upon calling
            this method.
        """

        for agent in agents:
            x, y = self.get_random_position()
            agent.x = x
            agent.y = y
            self.agents.append(agent)
            


if __name__ == '__main__':
    import utiles.agents.owner as owner
    room = Model(16, 16)

    # Example usage:
    file_path = 'assets/default_16x16_room.json'

    room.populate_room(file_path)

    '''gato = agent.Agent("Gato", 7, 7)
    room.generate_agents(gato)'''

    room.agents_random_spawn(owner.Owner("Owner", 7, 7))

    for row in room.matrix:
        for element in row:
            if element != 0:
                print(element._literal_name, end=" ")
            else:
                print(element, end=" ")

        print()
    # print(room.matrix)
    # print(room.agents[0])

    # print(room.matrix[4][7])
    # room.move_object(7, 4, 1, 1)
    # print(room.matrix[1][1])
