import sys
sys.path.insert(0, '.')

from utiles.commons.openable import Openable

class Container(Openable):

    def __init__(self, x, y, literal_name, storage):
        Openable.__init__(self, x, y, literal_name)

        self._storage = storage  # Use a different name for the attribute

    @property
    def storage(self):
        return self._storage

    
    def add_storage(self, **keyitems):

        assert isinstance(self._storage, dict), "Storage is not a dictionary"

        for key, elem in keyitems.items():
            if not key in self._storage:
                self._storage[key] = elem
            else: 
                self._storage[key] += elem  

    def remove_stock(self, **keyitems):
            for key, elem in keyitems.items():
                if not key in self._storage:
                    raise ValueError("Key not found")
                else: 
                    self._storage[key] -= elem

    def __str__(self):
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

