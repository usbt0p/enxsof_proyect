from abc import ABC, abstractmethod

class Thing(ABC):
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def opaque(self):
        pass

    @property
    @abstractmethod
    def stackable(self):
        pass

    @property
    @abstractmethod
    def container(self):
        pass