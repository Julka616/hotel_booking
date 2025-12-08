import json
from pathlib import Path
from typing import List, Optional
from room import Room
from booking import Booking


class Hotel:
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.rooms: List[Room] = []
        self.bookings: List[Booking] = []
        self._load()

    def _load(self):
        rooms_file = self.data_dir / "rooms.json"
        bookings_file = self.data_dir / "bookings.json"
        if rooms_file.exists():
            with rooms_file.open("r", encoding="utf-8") as f:
                self.rooms = [Room(**r) for r in json.load(f)]
        if bookings_file.exists():
            with bookings_file.open("r", encoding="utf-8") as f:
                self.bookings = [Booking(**b) for b in json.load(f)]

    def save(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
        with (self.data_dir / "rooms.json").open("w", encoding="utf-8") as f:
            json.dump([r.__dict__ for r in self.rooms], f, indent=2, ensure_ascii=False)
        with (self.data_dir / "bookings.json").open("w", encoding="utf-8") as f:
            json.dump([b.__dict__ for b in self.bookings], f, indent=2, ensure_ascii=False)

    def add_room(self, room: Room):
        self.rooms.append(room)
        self.save()

    def add_booking(self, booking: Booking):
        self.bookings.append(booking)
        self.save()

    def find_room(self, room_id: int) -> Optional[Room]:
        for r in self.rooms:
            if r.id == room_id:
                return r
        return None
