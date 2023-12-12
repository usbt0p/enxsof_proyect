import sys
sys.path.insert(0, '.')

from utiles.commons.openable import Openable

class Container(Openable):
    """
    A class representing a container that can be opened and closed.

    Attributes:
        x (int): The x-coordinate of the container's position.
        y (int): The y-coordinate of the container's position.
        literal_name (str): The literal name of the container.
        storage (dict): The storage dictionary of the container.

    Methods:
        add_storage: Add items to the storage dictionary.
        remove_stock: Remove items from the storage dictionary.
    """

    def __init__(self, x, y, literal_name, storage):
        """
        Initialize a Container object.

        Args:
            x (int): The x-coordinate of the container.
            y (int): The y-coordinate of the container.
            literal_name (str): The literal name of the container.
            storage (Storage): The storage object associated with the container.
        """
        Openable.__init__(self, x, y, literal_name)

        self._storage = storage  # Use a different name for the attribute

    @property
    def storage(self):
        """
        Get the storage property of the container.

        Returns:
            The storage property of the container.
        """
        return self._storage

    def add_storage(self, **keyitems):
        """
        Add items to the storage dictionary.

        Args:
            **keyitems: Keyword arguments representing the items to be added to the storage dictionary.
                The key is the item's name and the value is the quantity.

        Raises:
            AssertionError: If the storage is not a dictionary.
        """
        assert isinstance(self._storage, dict), "Storage is not a dictionary"

        for key, elem in keyitems.items():
            if not key in self._storage:
                self._storage[key] = elem
            else: 
                self._storage[key] += elem  

    def remove_stock(self, **keyitems):
        """
        Remove items from the storage dictionary.

        Args:
            **keyitems: Keyword arguments representing the items to be removed from the storage dictionary.
                The key is the item's name and the value is the quantity.

        Raises:
            ValueError: If the key is not found in the storage dictionary.
        """
        for key, elem in keyitems.items():
            if not key in self._storage:
                raise ValueError("Key not found")
            else: 
                self._storage[key] -= elem

    def __str__(self):
            """
            Returns a string representation of the Container object.

            The string representation includes the base string representation
            obtained from the parent class, along with the storage information.

            Returns:
                str: The string representation of the Container object.
            """
            base_str = super().__str__()  # Call the parent class's __str__ method
            return '{}, storage={}'.format(base_str, self.storage)


if __name__ == '__main__':
    obj = Container(4, 4, "Thing", {})
    print(obj)
    obj.open()
    print(obj)
    obj.close()
    print(obj)

    obj.add_storage(thing1=1, thing2=2)
    print(obj)
    obj.add_storage(thing1=2, thing2=14)
    print(obj)
    obj.remove_stock(thing1=1, thing2=2)
    print(obj)
    obj.add_storage(manzanas=1, peras=2)
    print(obj)

