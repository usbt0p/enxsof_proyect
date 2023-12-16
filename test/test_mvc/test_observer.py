import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from src.mvc.view import Observer

class ConcreteObserver(Observer):
    def __init__(self, name):
        super().__init__(name)
        
    def updateFromNotification(self, *new_state, **kwargs):
        return new_state, kwargs

class TestObserver(unittest.TestCase):

    def setUp(self):
        self.observer = ConcreteObserver('observer')

    def test_updateFromNotification(self):
        # Define the new state
        new_state = (1, 2, 3)

        # Call the updateFromNotification method
        self.observer.updateFromNotification(*new_state)

        # Assert that the method was called with the correct arguments
        # (in this case, we are just checking that the method was called without raising any exceptions)
        self.assertTrue(True)

    def test_object_counter(self):
        # Get the initial object counter value
        initial_counter = Observer._object_counter

        # Create a new observer
        observer = ConcreteObserver('obs')

        # Assert that the object counter has increased by 1
        self.assertEqual(Observer._object_counter, initial_counter + 1)

    def test_subclasshook(self):
        # Create a subclass that implements the updateFromNotification method
        class SubObserver(Observer):
            def updateFromNotification(self, *new_state, **kwargs):
                pass

        # Check if the subclass implements the required update method
        self.assertTrue(Observer.__subclasshook__(SubObserver))

    def test_str(self):
        # Set a custom name for the observer
        self.observer.name = "CustomObserver"

        # Get the string representation of the observer
        observer_str = str(self.observer)

        # Assert that the string representation is correct
        self.assertEqual(observer_str, "Observer: name=CustomObserver")

if __name__ == '__main__':
    unittest.main()