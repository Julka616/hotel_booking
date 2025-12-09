import unittest
from booking import Booking

class TestBooking(unittest.TestCase):
    def test_booking_initialization(self):
        booking = Booking(1, 101, "Alice", "2025-12-10", "2025-12-12")
        self.assertEqual(booking.room_id, 101)
        self.assertEqual(booking.user_name, "Alice")

if __name__ == "__main__":
    unittest.main()
