from Object import Object
import json
"""
    Model class.
    This class represents a room in the pyhton project.
"""
class Model():
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.room = self.generate_empty_room()
    
    
    def generate_empty_room(self):
        """
        Generates an empty room.
        Returns: a bidimensional zeros list with the size of the room
        """
        return [[0] * self.x_size for _ in range(self.y_size)]

        
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
    room = Model(4, 4)
    print(room.room)
    obj = Object("Wall", False, True)
    print(obj)
    for elem in room.room:
        print(elem)
    '''
    a = obj.collision
    b = obj._collision
    
    print(a, b)
    obj.collision = False
    print(obj)'''

        # Example usage:
    file_path = 'src/room/default_4x4_room.json'
    json_data = room.read_grid_config_file(file_path)

    if json_data is not None:
        print("JSON data:")
        for elem in json_data:
            print(elem)
        
    