from hotel import Hotel
from room import Room


def test_hotel_add_room(tmp_path):
    data_dir = tmp_path / "data"
    h = Hotel(str(data_dir))
    r = Room(id=10, number="200", type="suite", price=300.0)
    h.add_room(r)
    assert any(room.id == 10 for room in h.rooms)
