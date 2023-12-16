import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from utiles.commons.nurse import Nurse
from utiles.commons.owner import Owner
from utiles.objects.thing import Thing

class TestNurse(unittest.TestCase):

    def setUp(self):
        self.nurse = Nurse("Nurse", 0, 0, 5, 5)

    def test_nurse_initialization(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        self.assertEqual(nurse.name, "Nurse")
        self.assertEqual(nurse.x, 0)
        self.assertEqual(nurse.y, 0)
        self.assertEqual(nurse.battery, (100, 1, 0, [5, 5]))
        self.assertEqual(nurse.status, "Idle")

    def test_nurse_charge_battery(self):
        self.nurse.nurse_charge_battery()
        self.assertTrue(self.nurse.charging)
        self.assertEqual(self.nurse.charging_time, 0)
        self.assertEqual(self.nurse.status, "Charging")
        self.assertEqual(self.nurse.battery, (100, 1, 0, [5, 5]))

    def test_nurse_pick_object_success(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        thing = Thing(0, 0, "Item")
        self.assertTrue(nurse.nurse_pick_object(thing))
        self.assertEqual(len(nurse.inventory), 1)

    def test_nurse_pick_object_fail(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        thing = Thing(1, 1, "Item")
        self.assertFalse(nurse.nurse_pick_object(thing))
        self.assertEqual(len(nurse.inventory), 0)

    def test_nurse_drop_object(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        thing = Thing(0, 0, "Item")
        nurse.nurse_pick_object(thing)
        dropped_object = nurse.nurse_drop_object(thing)
        self.assertEqual(len(nurse.inventory), 0)
        self.assertEqual(dropped_object, thing)

    def test_manhattan_distance_to_owner(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        owner = Owner("John", 3, 3)
        distance = nurse.manhattan_distance_to_owner(owner)
        self.assertEqual(distance, 6)

    def test_updateFromNotification(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        new_state = (1, 1, 0, [5, 5])
        nurse.updateFromNotification(*new_state)
        self.assertEqual(nurse.x, 0)
        self.assertEqual(nurse.y, 0)
        self.assertEqual(nurse.battery, (100, 1, 0, [5, 5]))
        self.assertEqual(nurse.status, "Idle")

    def test_nurse_make_emergency_call(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        owner = Owner("John", 3, 3)
        self.assertTrue(nurse.make_emergency_call(owner))
        # Assert that the nurse's status has changed to "Emergency Call"
        self.assertEqual(nurse.status, "Emergency Call")

    def test_nurse_perform_resuscitation_exercise(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        owner = Owner("John", 3, 3)
        self.assertTrue(nurse.perform_resuscitation_exercise(owner))
        # Assert that the nurse's status has changed to "Resuscitation Exercise"
        self.assertEqual(nurse.status, "Resuscitation Exercise")

    def test_nurse_perform_action_on_vital_signs_change(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        owner = Owner("John", 3, 3)
        owner.vital_signs = {"heart_rate": 80, "blood_pressure": 120}
        
        # Simulate an anomalous variation in the owner's vital signs
        owner.vital_signs["heart_rate"] = 150
        
        # Assert that the nurse performs a specific action
        self.assertTrue(nurse.perform_action_on_vital_signs_change(owner))
        self.assertEqual(nurse.status, "Emergency Call")

    def test_nurse_perform_action_on_vital_signs_change_no_action(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        owner = Owner("John", 3, 3)
        owner.vital_signs = {"heart_rate": 80, "blood_pressure": 120}
        
        # Simulate a normal variation in the owner's vital signs
        owner.vital_signs["heart_rate"] = 90
        
        # Assert that the nurse does not perform any action
        self.assertFalse(nurse.perform_action_on_vital_signs_change(owner))
        self.assertEqual(nurse.status, "Idle")

    def test_nurse_get_battery_status(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        battery_status = nurse.battery
        self.assertEqual(battery_status, (100, 1, 0, [5, 5]))

    def test_nurse_charge_battery(self):
        nurse = Nurse("Nurse", 0, 0, 5, 5)
        nurse.battery = (10, 1, 0, [5, 5])  # Set battery level to low
        nurse.nurse_charge_battery()
        self.assertTrue(nurse.charging)
        self.assertEqual(nurse.charging_time, 0)
        self.assertEqual(nurse.status, "Charging")
        self.assertEqual(nurse.battery, (100, 1, 0, [5, 5]))

if __name__ == '__main__':
    unittest.main()