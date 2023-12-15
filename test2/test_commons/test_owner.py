import unittest
from utiles.commons.owner import Owner
from utiles.commons.thing import Thing

class TestOwner(unittest.TestCase):

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
        thing = Thing(1, 1, "Item")
        self.assertFalse(owner.agent_pick_object(thing))
        self.assertEqual(len(owner.inventory), 0)

    def test_agent_drop_object(self):
        owner = Owner("John", 0, 0)
        thing = Thing(0, 0, "Item")
        owner.agent_pick_object(thing)
        dropped_object = owner.agent_drop_object()
        self.assertEqual(len(owner.inventory), 0)
        self.assertEqual(dropped_object, thing)

if __name__ == '__main__':
    unittest.main()
