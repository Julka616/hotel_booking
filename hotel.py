import json
from room import Room
from booking import Booking

class Hotel:
    def __init__(self, rooms_file='data/rooms.json', bookings_file='data/bookings.json'):
        self.rooms_file = rooms_file
        self.bookings_file = bookings_file
        self.rooms = self.load_rooms()
        self.bookings = self.load_bookings()

    def load_rooms(self):
        with open(self.rooms_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Room(**room) for room in data]

    def load_bookings(self):
        with open(self.bookings_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Booking(**booking) for booking in data]

    def save_rooms(self):
        with open(self.rooms_file, 'w', encoding='utf-8') as f:
            json.dump([room.__dict__ for room in self.rooms], f, indent=2, ensure_ascii=False)

    def save_bookings(self):
        with open(self.bookings_file, 'w', encoding='utf-8') as f:
            json.dump([booking.__dict__ for booking in self.bookings], f, indent=2, ensure_ascii=False)

    def list_available_rooms(self):
        return [room for room in self.rooms if room.available]

    def add_booking(self, user_name, room_id, start_date, end_date):
        room = next((r for r in self.rooms if r.id == room_id), None)
        if room and room.available:
            new_id = max([b.id for b in self.bookings], default=0) + 1
            booking = Booking(new_id, room_id, user_name, start_date, end_date)
            self.bookings.append(booking)
            room.available = False
            self.save_bookings()
            self.save_rooms()
            return booking
        return None

    def cancel_booking(self, booking_id):
        booking = next((b for b in self.bookings if b.id == booking_id), None)
        if booking:
            self.bookings.remove(booking)
            room = next((r for r in self.rooms if r.id == booking.room_id), None)
            if room:
                room.available = True
            self.save_bookings()
            self.save_rooms()
            return True
        return False
