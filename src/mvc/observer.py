import sys
sys.path.insert(0, '.')

from abc import ABC
from abc import abstractmethod

class Observer(ABC):
    
    _object_counter = 0

    def __init__(self, name=None) -> None:
        self.name = name if name else self.__class__.__name__ + str(Observer._object_counter)
        Observer._object_counter += 1

    @abstractmethod
    def updateFromNotification(self, *new_state, **kwargs):
        """
        Called by the concrete Observable when data has changed passing its state.
        :param new_state: The new state.
        :type new_state: A tuple of arbitrary content.
        """
        pass

    @property
    def object_counter(self) -> int:
        """
        Returns the number of created objects of this class.
        :return: the number of created objects class attribute.
        """
        return Observer._object_counter

    @classmethod
    def __subclasshook__(cls, sub_class):
            """
            Checks if the given subclass implements the required update method.

            Args:
                cls: The class object.
                sub_class: The subclass to be checked.

            Returns:
                True if the subclass implements the update method, False otherwise.
            """
            return any(cls.updateFromNotification.__str__() in klazz.__dict__ for klazz in sub_class.__mro__) != []
    

    def __str__(self) -> str:
        """
        Returns the name of the observer.
        :return: The name of the observer.
        """
        return f'Observer: name={self.name}'
