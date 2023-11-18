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

class Observable(object):

    def __init__(self, name = None):
        """
        :param name: A name may be set for this class, but if not set the class name is used.
        """
        self.name = name if name else self.__class__.__name__
        self._observers = set()  # use a set to avoid duplicate registered observers

    def attach(self, observer):
        """
        Attach an Observer wanting to be notified of updates from the concrete Observable.
        Note that the same object can only be attached once, but several different objects
        may.
        :param observer: The observer object to be attached.
        :type observer: Observer
        :raise ValueError is raised if the observer object is not of type Observer
        """
        if not isinstance(observer, Observer):
            raise ValueError('You need to pass a valid Observer class object')
        self._observers.add(observer)

    def detach(self, observer):
        """
        Detaches an Observer object from listening to updates from the concrete Observable.
        :param observer: The observer object to be removed.
        :type observer: Observer
        """
        if observer in self._observers:
            self._observers.discard(observer)

    def notify(self, *new_state):
        """
        The new state is updated to all registered Observers.
        :param new_state: The new state.
        :type new_state: A tuple of arbitrary content.
        """
        for observer in self._observers:
            observer.update(new_state)