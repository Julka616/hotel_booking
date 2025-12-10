from typing import Optional
from room import Room
from booking import Booking
from repository import DataStore, FileDataStore


class Hotel:
    """Klasa `Hotel` zarządza logiką rezerwacji (SRP: logika biznesowa oddzielona od IO).

    Przyjmuje implementację `DataStore` przez wstrzyknięcie zależności (DIP).
    Domyślnie używa `FileDataStore`, ale można podać np. mock w testach.
    """

    def __init__(self, rooms_file: str = 'data/rooms.json', bookings_file: str = 'data/bookings.json', datastore: Optional[DataStore] = None):
        # jeśli nie podano datastore, użyj domyślnego FileDataStore
        if datastore is None:
            datastore = FileDataStore(rooms_file, bookings_file)
        self.datastore: DataStore = datastore
        self.rooms = self.datastore.load_rooms()
        self.bookings = self.datastore.load_bookings()

    def save_rooms(self):
        """Zapisuje listę pokoi przez DataStore."""
        self.datastore.save_rooms(self.rooms)

    def save_bookings(self):
        """Zapisuje listę rezerwacji przez DataStore."""
        self.datastore.save_bookings(self.bookings)

    def list_available_rooms(self):
        """Zwraca listę dostępnych pokoi."""
        return [room for room in self.rooms if room.available]

    def add_booking(self, user_name, room_id, start_date, end_date):
        """Tworzy rezerwację jeśli pokój jest dostępny; zwraca obiekt Booking lub None."""
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
        """Anuluje rezerwację i oznacza pokój jako dostępny. Zwraca True/False."""
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
