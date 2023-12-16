import unittest
from utiles.agents.owner import Owner
from utiles.objects.thing import Thing
from unittest.mock import MagicMock

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner = Owner("John", 0, 0)

    def test_owner_initialization(self):
        owner = Owner("John", 0, 0)
        self.assertEqual(owner.name, "John")
        self.assertEqual(owner.x, 0)
        self.assertEqual(owner.y, 0)
        self.assertEqual(len(owner.inventory), 0)

    def test_agent_pick_object_success(self):
        owner = Owner("John", 0, 0)
        thing = Thing(0, 0, "Item")
        self.assertTrue(owner.agent_pick_object(thing))
        self.assertEqual(len(owner.inventory), 1)

    def test_agent_pick_object_fail(self):
        owner = Owner("John", 0, 0)
        thing = Thing(1, 1, "Item") # asumiendo que la función se ejecuta solo cuando está encuima del objeto
        self.assertFalse(owner.agent_pick_object(thing))
        self.assertEqual(len(owner.inventory), 0)

    def test_agent_drop_object(self):
        owner = Owner("John", 0, 0)
        thing = Thing(0, 0, "Item")
        owner.agent_pick_object(thing)
        dropped_object = owner.agent_drop_object(thing)
        self.assertEqual(len(owner.inventory), 0)
        self.assertEqual(dropped_object, thing)

    def test_vitals_setter(self):
        # Test setting vitals
        self.owner.vitals_setter(70, "130/90", 37.2, 18, 95, 14)
        self.assertEqual(self.owner.vitals, (70, "130/90", 37.2, 18, 95, 14))

    def test_vitals(self):
        # Test getting vitals
        self.assertEqual(self.owner.vitals, (60, "120/80", 36.6, 16, 98, 15))

    def test_agent_interact_with_other_agent(self):
        # Test interaction with another agent
        other_agent = MagicMock()
        self.owner.agent_interact_with_other_agent(other_agent)
        other_agent.interact.assert_called_once_with(self.owner)

    def test_owner_move_to_coordinates(self):
        # Test owner moving to coordinates
        self.owner.move_to_coordinates(5, 5)
        self.assertEqual(self.owner.x, 5)
        self.assertEqual(self.owner.y, 5)
        self.assertEqual(self.owner.events[-1], "OwnerMovingToCoordinates")

    def test_owner_move_object(self):
        # Test owner moving object
        thing = Thing(0, 0, "Item")
        self.owner.agent_pick_object(thing)
        self.owner.move_object(10, 10)
        self.assertEqual(thing.x, 10)
        self.assertEqual(thing.y, 10)
        self.assertEqual(self.owner.events[-1], "OwnerMovingObject")

    def test_owner_faint(self):
        # Test owner fainting
        self.owner.faint()
        self.assertEqual(self.owner.events[-1], "OwnerFainted")

    def test_owner_wake_up(self):
        # Test owner waking up
        self.owner.wake_up()
        self.assertEqual(self.owner.events[-1], "OwnerWokeUp")

    def test_owner_die(self):
        # Test owner dying
        self.owner.die()
        self.assertEqual(self.owner.events[-1], "OwnerDied")

if __name__ == '__main__':
    unittest.main()
