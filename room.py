from dataclasses import dataclass

@dataclass
class Room:
    id: int
    number: str
    type: str
    price: float
