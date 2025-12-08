class Room:
    def __init__(self, id, name, type, price, available=True):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.available = available
