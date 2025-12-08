from booking import Booking


def test_booking_dataclass():
    b = Booking(id=1, room_id=1, guest_name="Jan", check_in="2025-12-01", check_out="2025-12-03")
    assert b.room_id == 1
    assert b.guest_name == "Jan"
