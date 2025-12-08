from dataclasses import dataclass

@dataclass
class Booking:
    id: int
    room_id: int
    guest_name: str
    check_in: str  # ISO date YYYY-MM-DD
    check_out: str
