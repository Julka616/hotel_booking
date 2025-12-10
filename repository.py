"""
Moduł odpowiedzialny za dostęp do danych (IO).
Zgodnie z zasadą SRP wydzielamy operacje wczytywania/zapisu JSON z logiki biznesowej.
Definiujemy abstrakcyjny `DataStore` oraz implementację `FileDataStore`.
"""
from abc import ABC, abstractmethod
import json
from typing import List
from room import Room
from booking import Booking


class DataStore(ABC):
    """Abstrakcja źródła danych — pozwala podmienić implementację (np. mock w testach)."""

    @abstractmethod
    def load_rooms(self) -> List[Room]:
        pass

    @abstractmethod
    def load_bookings(self) -> List[Booking]:
        pass

    @abstractmethod
    def save_rooms(self, rooms: List[Room]):
        pass

    @abstractmethod
    def save_bookings(self, bookings: List[Booking]):
        pass


class FileDataStore(DataStore):
    """Implementacja DataStore zapisująca/odczytująca pliki JSON.

    Użycie FileDataStore pozwala na DI w klasie Hotel — zachowujemy otwartość na rozszerzenia
    (np. inna implementacja DataStore) bez modyfikowania logiki Hotel.
    """

    def __init__(self, rooms_file: str = 'data/rooms.json', bookings_file: str = 'data/bookings.json'):
        self.rooms_file = rooms_file
        self.bookings_file = bookings_file

    def load_rooms(self) -> List[Room]:
        try:
            with open(self.rooms_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        return [Room(**r) for r in data]

    def load_bookings(self) -> List[Booking]:
        try:
            with open(self.bookings_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        return [Booking(**b) for b in data]

    def save_rooms(self, rooms: List[Room]):
        with open(self.rooms_file, 'w', encoding='utf-8') as f:
            json.dump([r.__dict__ for r in rooms], f, indent=2, ensure_ascii=False)

    def save_bookings(self, bookings: List[Booking]):
        with open(self.bookings_file, 'w', encoding='utf-8') as f:
            json.dump([b.__dict__ for b in bookings], f, indent=2, ensure_ascii=False)
