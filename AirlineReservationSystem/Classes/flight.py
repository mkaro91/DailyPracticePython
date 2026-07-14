# flight.py

class Flight:
    def __init__(self, flight_number: str, destination: str, departure_date: str, departure_time: str, capacity: int, seats_available: int):
        self.flight_number = flight_number.upper()
        self.destination = destination.title()
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.capacity = capacity
        self.seats_available = seats_available
    
    @property
    def is_full(self):
        return self.seats_available == 0
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            flight_number = data['flight_number'],
            destination = data['destination'],
            departure_date = data['departure_date'],
            departure_time = data['departure_time'],
            capacity = data['capacity'],
            seats_available = data['seats_available']
        )
    
    def to_dict(self):
        return {
            "flight_number": self.flight_number,
            "destination": self.destination,
            "departure_date": self.departure_date,
            "departure_time": self.departure_time,
            "capacity": self.capacity,
            "seats_available": self.seats_available
        }
    
    def display(self):
        print(f'\n{"-" * 25}')
        print("Flight", self.flight_number)
        print(self.destination)

        print("\nDeparture:")
        print(self.departure_date)
        print(self.departure_time)

        print("\nCapacity:", self.capacity)
        print("Available:", self.seats_available)
        print("-" * 25)
    
    def generate_seat_number(self):
        return self.capacity - self.seats_available + 1