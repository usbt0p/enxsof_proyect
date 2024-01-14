import sys
sys.path.insert(0, '.')

import unittest
import subprocess
from utiles.objects import (mixed, movable, openable,thing)
from utiles.agents import (owner, agent, nurse)
from utiles.commons import (movementSystem, vitalsGenerator)
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



if __name__ == '__main__':
    

    def test_execute_main(self):
        import sys
        sys.path.insert(0, '.')

        import os
        import subprocess

        if __name__ == "__main__":
            # Establish PYTHONPATH on the script location
            os.environ['PYTHONPATH'] = '.'
        

            result = subprocess.run(["python", "src/main.py"], shell=True, text=True)
        self.assertEqual(result.returncode, 0)

    unittest.main()