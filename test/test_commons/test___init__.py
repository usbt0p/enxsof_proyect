import sys
sys.path.insert(0, '.')

import unittest
import subprocess
from utiles import mixed, movable, owner
from utiles.agents import agent
from utiles.commons import (movementSystem)
from src.mvc import (model, view, controller, observer, subject)
from utiles.objects import openable, thing

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