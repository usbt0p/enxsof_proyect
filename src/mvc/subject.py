import sys
sys.path.insert(0, '.')

from src.mvc import observer
from abc import ABC

class Subject(ABC):
    """
    Represents a subject in the observer pattern.

    Attributes:
        _observers (set): A set of observers attached to the subject.

    Methods:
        attach(*observers: list) -> None:
            Attaches one or more observers to the subject.

        detach(observer: ob.Observer) -> None:
            Detaches an observer from the subject.

        notifyAll(*args: list, **kwargs: dict) -> None:
            Notifies all the observers by calling their update method with the given arguments.

        notify(observer, *args: list, **kwargs: dict) -> None:
            Notifies the observer by calling its update_observer method with the provided arguments.
    """
    def __init__(self, *args:tuple, **kwargs:dict) -> None:
        self._observers = set()

    def attach(self, *observers:list) -> None:
        """
        Attaches one or more observers to the subject.

        Args:
            *observers (list): The observers to attach.

        Raises:
            TypeError: If an observer is not an instance of the Observer class.
        """
        for obs in observers:
            if not isinstance(obs, observer.Observer):
                raise TypeError('El observer debe ser una instancia de la clase Observer')
            else:
                self._observers.add(obs)

    def detach(self, observer:observer.Observer) -> None:
            """
            Detaches an observer from the subject.

            Args:
                observer (ob.Observer): The observer to detach.

            Returns:
                None
            """
            self._observers.discard(observer)

    def notifyAll(self, *args: list, **kwargs: dict) -> None:
        """
        Notifies all the observers by calling their update method with the given arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """

        for observer in self._observers:
            observer.updateFromNotification(*args, **kwargs)

    def notify(self, observer:observer, *args:list, **kwargs:dict) -> None:
        """
        Notifies the observer by calling its update_observer method with the provided arguments.

        Args:
            observer: The observer object to be notified.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            AssertionError: If the observer is not in the attached list.
        """
        assert observer in self._observers, 'Observer must be in attached list'
        observer.updateFromNotification(*args, **kwargs)


if "__main__" == __name__:

    # Crear sujeto
    subject = Subject()

    # Crear observadores
    view = observer.Observer('view')
    controller = observer.Observer('controller')

    # Adjuntar los observadores al sujeto
    subject.attach(view, controller)

    prueba = {'jeizee': 1}

    # Notificar a todos los observadores
    subject.notifyAll('¡Hola, Observadores!')
    subject.notify(view, prueba)
