import unittest
import subprocess
from utiles.commons import (thing, owner, openable, movable, mixed, movementSystem, agent)
from src.mvc import (model, view, controller, observer, subject)

class TestExecute(unittest.TestCase):

    # check if if all imports are correct
    def test_import_commons(self):
        self.assertIsNotNone(thing)
        self.assertIsNotNone(owner)
        self.assertIsNotNone(openable)
        self.assertIsNotNone(movable)
        self.assertIsNotNone(mixed)
        self.assertIsNotNone(movementSystem)
        self.assertIsNotNone(agent)
        self.assertIsNotNone(model)
        self.assertIsNotNone(view)
        self.assertIsNotNone(controller)
        self.assertIsNotNone(observer)
        self.assertIsNotNone(subject)

    def test_execute_main(self):
        result = subprocess.run(["python", "src/mvc/main.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        # Add more assertions to validate the output if needed


if __name__ == '__main__':
    unittest.main()