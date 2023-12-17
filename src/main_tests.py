import sys
sys.path.insert(0, '.')

import unittest
from test.test_mvc import (test_controller, test_model, test_observer, test_subject, test_view)
from test.test_commons import (test_initialize, test_agents, test_mixed, test_movable, 
                               test_movementSystem, test_nurse, test_openable, 
                               test_owner, test_thing, test_vitalsGenerator)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(test_controller))
    suite.addTests(loader.loadTestsFromModule(test_model))
    suite.addTests(loader.loadTestsFromModule(test_observer))
    suite.addTests(loader.loadTestsFromModule(test_subject))
    suite.addTests(loader.loadTestsFromModule(test_view))


    suite.addTests(loader.loadTestsFromModule(test_initialize))
    suite.addTests(loader.loadTestsFromModule(test_agents))
    suite.addTests(loader.loadTestsFromModule(test_mixed))
    suite.addTests(loader.loadTestsFromModule(test_movable))
    suite.addTests(loader.loadTestsFromModule(test_movementSystem))
    suite.addTests(loader.loadTestsFromModule(test_nurse))
    suite.addTests(loader.loadTestsFromModule(test_openable))
    suite.addTests(loader.loadTestsFromModule(test_owner))
    suite.addTests(loader.loadTestsFromModule(test_thing))
    suite.addTests(loader.loadTestsFromModule(test_vitalsGenerator))



    runner = unittest.TextTestRunner()
    runner.run(suite)