from abc import ABCMeta
from abc import abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta

    _object_counter = 0

    def __init__(self, name=None):
        self.name = name if name else self.__class__.__name__ + str(Observer._object_counter)
        Observer._object_counter += 1

    @abstractmethod
    def update(self, *new_state):
        """
        Called by the concrete Observable when data has changed passing its state.
        :param new_state: The new state.
        :type new_state: A tuple of arbitrary content.
        """
        pass

    @property
    def object_counter(self):
        """
        Returns the number of created objects of this class.
        :return: the number of created objects class attribute.
        """
        return Observer._object_counter

    @classmethod
    def __subclasshook__(cls, sub_class):  # correct behavior when isinstance, issubclass is called
        return any(cls.update.__str__() in klazz.__dict__ for klazz in sub_class.__mro__) != []
    
class ConcreteObserver(Observer):
    def __init__(self, name):
        super().__init__(name)

    def update(self, *new_state):
        print(f'{self.name} ha recibido una actualización: {new_state}')