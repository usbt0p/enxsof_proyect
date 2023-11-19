from observer import Observer

class Subject:
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        if not isinstance(observer, Observer):
            raise TypeError('El observer debe ser una instancia de la clase Observer')
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)

if "__main__" == __name__:

    from observer import ConcreteObserver

    # Crear un sujeto
    subject = Subject()

    # Crear observadores
    observer1 = ConcreteObserver('Observer1')
    observer2 = ConcreteObserver('Observer2')

    # Adjuntar los observadores al sujeto
    subject.attach(observer1)
    subject.attach(observer2)

    # Notificar a todos los observadores
    subject.notify('¡Hola, Observadores!')
