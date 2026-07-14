# reservation.py

class Reservation:
    def __init__(self, reservation_id, flight_number, passport_number, seat_number):
        self.id = reservation_id
        self.flight_number = flight_number
        self.passport_number = passport_number
        self.seat_number = seat_number
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            reservation_id = data['id'],
            flight_number = data['flight_number'],
            passport_number = data['passport_number'],
            seat_number = data['seat_number']
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'flight_number': self.flight_number,
            'passport_number': self.passport_number,
            'seat_number': self.seat_number
        }
    
    def get_passenger_name(self, passengers):
        for passenger in passengers:
            if passenger.passport_number == self.passport_number:
                return passenger.name
    
    def get_flight_destination(self, flights):
        for flight in flights:
            if flight.flight_number == self.flight_number:
                return flight.destination

    def display(self, flights, passengers):
        print(f"\nReservation {self.id}")
        
        print("\nPassenger:")
        print(self.get_passenger_name(passengers))

        print("\nPassport:")
        print(self.passport_number)
        
        print("\nFlight:")
        print(self.flight_number)

        print("\nDestination:")
        print(self.get_flight_destination(flights))

        print("\nSeat:")
        print(self.seat_number)