from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    '''We define a 'template' for our classes using an abstract class.
    All classes inheriting from Subject must implement it's methods.'''
	
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def addObserver(self):
        ...

    @abstractmethod
    def removeObserver(self):
        ...

    @abstractmethod
    def addElem(self):
        ...

    @abstractmethod
    def removeElem(self):
        ...

    @abstractmethod
    def notifyObservers(self):
        ...

    @abstractmethod
    def getSujetos(self):
        ...

    @abstractmethod
    def setSujetos(self):
        ...

	
		