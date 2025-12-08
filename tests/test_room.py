from room import Room


def test_room_dataclass():
    r = Room(id=1, number="101", type="single", price=100.0)
    assert r.id == 1
    assert r.number == "101"
