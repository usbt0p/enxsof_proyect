import sys
sys.path.insert(0, '.')


from utiles.commons.openable import Openable

class Mixed(Openable):
    def __init__(self, x:int, y:int, literal_name):
        """
        Initializes a Mixed object.

        Args:
            x (int): The x-coordinate of the Mixed object.
            y (int): The y-coordinate of the Mixed object.
            literal_name: The literal name of the Mixed object.

        """
        Openable.__init__(self, x, y, literal_name)

if __name__ == '__main__':
    obj = Mixed(4, 4, "Thing")

    print(dir(obj))