import unittest
from room import Room

class TestRoom(unittest.TestCase):
    def test_room_initialization(self):
        room = Room(1, "Room A", "Single", 100)
        self.assertEqual(room.id, 1)
        self.assertEqual(room.name, "Room A")
        self.assertTrue(room.available)

if __name__ == "__main__":
    unittest.main()
