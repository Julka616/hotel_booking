from hotel import Hotel
from utils import validate_date

def main():
    hotel = Hotel()
    while True:
        print("\n1. List available rooms")
        print("2. Add booking")
        print("3. Cancel booking")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            rooms = hotel.list_available_rooms()
            for room in rooms:
                print(f"{room.id}: {room.name} ({room.type}) - ${room.price}")
        elif choice == "2":
            name = input("Your name: ")
            room_id = int(input("Room ID: "))
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            if validate_date(start) and validate_date(end):
                booking = hotel.add_booking(name, room_id, start, end)
                if booking:
                    print("Booking added!")
                else:
                    print("Room not available.")
            else:
                print("Invalid dates.")
        elif choice == "3":
            booking_id = int(input("Booking ID to cancel: "))
            if hotel.cancel_booking(booking_id):
                print("Booking canceled!")
            else:
                print("Booking not found.")
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
