import sys
sys.path.insert(0, '.')

import unittest
from test/test_mvc import test_controller, test_model, test_observer, test_subject, test_view
from test/test_commons import test__init__, test_agents, test_mixed, test_movable, test_movementSystem, test_nurse, test_openable, test_owner, test_thing, test_vitalsGenerator

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(test_module1))
    suite.addTests(loader.loadTestsFromModule(test_module2))

    runner = unittest.TextTestRunner()
    runner.run(suite)