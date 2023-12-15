import unittest
import subprocess

class TestExecute(unittest.TestCase):

    def test_execute_main(self):
        result = subprocess.run(["python", "src/main.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        # Add more assertions to validate the output if needed

    def test_import_commons(self):
        import utiles.commons
        self.assertIsNotNone(utiles.commons.thing)
        self.assertIsNotNone(utiles.commons.owner)
        self.assertIsNotNone(utiles.commons.openable)
        self.assertIsNotNone(utiles.commons.movable)
        self.assertIsNotNone(utiles.commons.mixed)
        self.assertIsNotNone(utiles.commons.movementSystem)
        self.assertIsNotNone(utiles.commons.agent)

if __name__ == '__main__':
    unittest.main()