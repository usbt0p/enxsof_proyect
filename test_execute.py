import unittest
import subprocess

class TestExecute(unittest.TestCase):

    def test_execute_main(self):
        result = subprocess.run(["python", "src/main.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        # Add more assertions to validate the output if needed

if __name__ == '__main__':
    unittest.main()