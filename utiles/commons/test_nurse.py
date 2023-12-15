import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from utiles.commons.nurse import Nurse

class TestNurse(unittest.TestCase):

    def setUp(self):
        self.nurse = Nurse("Nurse1", 0, 0, 1, 1)

    def test_nurse_charge_battery(self):
        self.nurse.nurse_charge_battery()
        self.assertTrue(self.nurse.charging)
        self.assertEqual(self.nurse.charging_time, 0)
        self.assertEqual(self.nurse.status, "Charging")
        self.assertEqual(self.nurse.battery, eval("100, 1, 0, [1, 1]"))

    def test_nurse_pick_object(self):
        object = MagicMock()
        object.x = 0
        object.y = 0
        self.assertTrue(self.nurse.nurse_pick_object(object))
        self.assertIn(object, self.nurse.inventory)

    def test_nurse_pick_object_invalid_location(self):
        object = MagicMock()
        object.x = 1
        object.y = 1
        self.assertFalse(self.nurse.nurse_pick_object(object))
        self.assertNotIn(object, self.nurse.inventory)

    def test_nurse_drop_object(self):
        object = MagicMock()
        self.nurse.inventory.append(object)
        self.assertEqual(self.nurse.nurse_drop_object(object), object)
        self.assertNotIn(object, self.nurse.inventory)

    def test_manhattan_distance_to_owner(self):
        owner = MagicMock()
        owner.x = 2
        owner.y = 2
        pathPlanning = MagicMock()
        pathPlanning.heuristic = MagicMock(return_value=4)
        self.nurse.pathPlanning = pathPlanning
        self.assertEqual(self.nurse.manhattan_distance_to_owner(owner), 4)

if __name__ == '__main__':
    unittest.main()