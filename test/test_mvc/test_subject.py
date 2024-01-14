import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from src.mvc.subject import Subject
from src.mvc.observer import Observer

class ConcreteObserver(Observer):
        def __init__(self) -> None:
            super().__init__()
        def updateFromNotification(self, *args, **kwargs):
            pass

class ConcreteSubject(Subject):
    def __init__(self) -> None:
        super().__init__()
    

class TestSubject(unittest.TestCase):
    

    def setUp(self) -> None:
        self.subject = Subject()
        

    def test_attach(self) -> None:
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)

        self.assertIn(observer1, self.subject._observers)
        self.assertIn(observer2, self.subject._observers)

    def test_attach_invalid_observer(self) -> None:
        obs = ConcreteObserver()
        sub = ConcreteSubject()
        false_obs = 'mock'

        sub.attach(obs)
        print(sub._observers)

        sub.attach(false_obs)
        print(sub._observers)

    def test_detach(self) -> None:
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)
        self.subject.detach(observer1)

        self.assertNotIn(observer1, self.subject._observers)
        self.assertIn(observer2, self.subject._observers)

    def test_notifyAll(self) -> None:
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)
        self.subject.notifyAll('Hello', name='John')

        observer1.updateFromNotification.assert_called_once_with('Hello', name='John')
        observer2.updateFromNotification.assert_called_once_with('Hello', name='John')

    def test_notify(self) -> None:
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)
        self.subject.notify(observer1, 'Hello', name='John')

        observer1.updateFromNotification.assert_called_once_with('Hello', name='John')
        observer2.updateFromNotification.assert_not_called()

if __name__ == '__main__':
    unittest.main()