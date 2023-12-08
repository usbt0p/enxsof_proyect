import sys
sys.path.insert(0, '.')

from abc import ABCMeta
from abc import abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta

    _object_counter = 0

    def __init__(self, name=None) -> None:
        self.name = name if name else self.__class__.__name__ + str(Observer._object_counter)
        Observer._object_counter += 1

    @property
    def object_counter(self) -> int:
        """
        Returns the number of created objects of this class.
        :return: the number of created objects class attribute.
        """
        return Observer._object_counter

    @classmethod
    def __subclasshook__(cls, sub_class):  # correct behavior when isinstance, issubclass is called
        return any(cls.update.__str__() in klazz.__dict__ for klazz in sub_class.__mro__) != []
    

    def update_self(self, *new_state, **keyword_states) -> str:
        '''
        Default method for updating the observer with the new state.
        Override in each child for custom behavior.
        '''
        #print(f'{self.name} ha recibido una actualización: {new_state}')
        # if they are present, add the states and keyword states to an fstring and return it
        if new_state:
            new_state = f' {new_state}'
        else:
            new_state = ''
        if keyword_states:
            keyword_states = f' {keyword_states}'
        else:
            keyword_states = ''
        print(f'{self.name} ha recibido una actualización:{new_state}{keyword_states}')