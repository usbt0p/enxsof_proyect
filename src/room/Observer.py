from abc import abstractmethod


class Observer():

    @abstractmethod
    def subscribe_to(self):
        pass

    @abstractmethod
    def update(self):
        pass
