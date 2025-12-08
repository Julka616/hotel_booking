from hotel import Hotel
from room import Room
from booking import Booking
import os


def main():
    base = os.path.join(os.path.dirname(__file__), "data")
    h = Hotel(base)
    print("Rooms:", h.rooms)
    print("Bookings:", h.bookings)


if __name__ == "__main__":
    main()
