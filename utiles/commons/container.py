from utiles.commons.thing import Thing

class Container(Thing):

    # TODO mejorar la forma de activar los atributos interactive y colision automaticamente, de forma q no se puedan cambiar 
    def __init__(self, x, y, literal_name, storage, interactive=True, collision=True):
        super().__init__( x, y, literal_name, interactive, collision)
        self._storage = storage  # Use a different name for the attribute


    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value  # Use the same name as the attribute

    def __str__(self):
        base_str = super().__str__()  # Call the parent class's __str__ method
        return '{}, storage={}'.format(base_str, self.storage)

