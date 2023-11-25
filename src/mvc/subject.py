import sys
sys.path.insert(0, '.')

from src.mvc import observer as ob

class Subject:
    def __init__(self) -> None:
        self._observers = set()

    def attach(self, *observers:list) -> None:
        for obs in observers:
            if not isinstance(obs, ob.Observer):
                raise TypeError('El observer debe ser una instancia de la clase Observer')
            self._observers.add(obs)

    def detach(self, observer:ob.Observer) -> None:
        self._observers.discard(observer)

    def notifyAll(self, *args:list, **kwargs:dict) -> None:
        for observer in self._observers:
            observer.update(*args, **kwargs)

    def notify(self, observer, *args:list, **kwargs:dict) -> None:
        assert observer in self._observers, 'Observer must be in attached list'
        observer.update(*args, **kwargs)

if "__main__" == __name__:

    # Crear un sujeto
    subject = Subject()

    # Crear observadores
    view = ob.ConcreteObserver('view')
    controller = ob.ConcreteObserver('controller')

    # Adjuntar los observadores al sujeto
    subject.attach(view, controller)

    # Notificar a todos los observadores
    subject.notifyAll('¡Hola, Observadores!')
    subject.notify(view, 'actualiza la vista')
