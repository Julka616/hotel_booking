class Room:
    def __init__(self, id, name, type, price, number=None, available=True):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.number = number
        self.available = available
