import unittest
from hotel import Hotel

class TestHotelIntegration(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()

    def test_list_available_rooms(self):
        rooms = self.hotel.list_available_rooms()
        self.assertIsInstance(rooms, list)

if __name__ == "__main__":
    unittest.main()
