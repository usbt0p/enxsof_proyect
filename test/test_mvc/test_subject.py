import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from src.mvc.subject import Subject
from src.mvc.observer import Observer

class TestSubject(unittest.TestCase):

    def setUp(self):
        self.subject = Subject()

    def test_attach(self):
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)

        self.assertIn(observer1, self.subject._observers)
        self.assertIn(observer2, self.subject._observers)

    def test_attach_invalid_observer(self):
        observer = "invalid_observer"

        with self.assertRaises(TypeError):
            self.subject.attach(observer)

    def test_detach(self):
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)
        self.subject.detach(observer1)

        self.assertNotIn(observer1, self.subject._observers)
        self.assertIn(observer2, self.subject._observers)

    def test_notifyAll(self):
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)
        self.subject.notifyAll('Hello', name='John')

        observer1.updateFromNotification.assert_called_once_with('Hello', name='John')
        observer2.updateFromNotification.assert_called_once_with('Hello', name='John')

    def test_notify(self):
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)

        self.subject.attach(observer1, observer2)
        self.subject.notify(observer1, 'Hello', name='John')

        observer1.updateFromNotification.assert_called_once_with('Hello', name='John')
        observer2.updateFromNotification.assert_not_called()

if __name__ == '__main__':
    unittest.main()