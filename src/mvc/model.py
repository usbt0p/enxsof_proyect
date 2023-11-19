from utiles.commons import *
from src.mvc.subject import Subject
import json

"""
    Model class.
    This class represents a room in the pyhton project.
"""
class Model(Subject):
    def __init__(self, x_size, y_size):
        super().__init__()
        self.x_size = x_size
        self.y_size = y_size
        self.matrix = self.generate_empty_room()
    
    
    def generate_empty_room(self):
        """
        Generates an empty room.
        Returns: a bidimensional zeros list with the size of the room
        """
        return [[0] * self.x_size for _ in range(self.y_size)]



    def populate_room(self, filepath):
        """
        Add decorations to the room.
        The decorations are represented by an id_decoration.
        Returns: a bidimensional list with the decorations added
        """

        config = self.read_grid_config_file(filepath)

        # Posible test de unidad
        '''print(self.y_size == len(config), self.y_size, len(config)) 
        print(self.x_size == len(config[0]), self.x_size, len(config[0]))'''

        assert self.y_size == len(config) and self.x_size == len(config[0]),\
              "Size of the map must be equal to size of the config file's map" 
        
        for y, row in enumerate(config): # TODO es posible q esto saque la "transpuesta" del mapa, veremos
            for x, literal in enumerate(row):
                match literal:
                    case "Wall":
                        self.matrix[y][x] = wall.Wall(x, y)
                    case "Air":
                        self.matrix[y][x] = air.Air(x, y)
                    case "Sofa":
                        self.matrix[y][x] = sofa.Sofa(x, y)
                    case "Door":
                        self.matrix[y][x] = door.Door(x, y)
                    case "Table":
                        self.matrix[y][x] = table.Table(x, y)
                    case "Fridge":
                        self.matrix[y][x] = fridge.Fridge(x, y)
                                      
        

    def read_grid_config_file(self, file_path):
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
    room = Model(16, 16)
    '''print(room.room)
    obj = Object("Wall", False, True)
    print(obj)
    for elem in room.room:
        print(elem)'''
    '''
    a = obj.collision
    b = obj._collision
    
    print(a, b)
    obj.collision = False
    print(obj)'''

        # Example usage:
    file_path = 'assets/default_16x16_room.json'
    '''    json_data = room.read_grid_config_file(file_path)

    if json_data is not None:
        print("JSON data:")
        for elem in json_data:
            print(elem)'''
    room.populate_room(file_path)
    print(room.matrix)
        
    