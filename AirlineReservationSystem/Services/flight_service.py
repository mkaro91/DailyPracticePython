import json
import os

from helpers import *

from Classes.flight import Flight

FLIGHT_SAVE = "data/flights.json"

def save_flights(flights):
    os.makedirs('data', exist_ok=True)
    data = [flight.to_dict() for flight in flights]

    with open(FLIGHT_SAVE, 'w') as f:
        json.dump(data, f, indent=2)

def load_flights():
    try:
        with open(FLIGHT_SAVE, 'r') as f:
            return [Flight.from_dict(flight) for flight in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def find_flight_by_number(flights, flight_number):
    for flight in flights:
        if flight.flight_number == flight_number:
            return flight
    return None

def add_flight(flights):
    prep_screen("=== Add Flight ===")

    # Prevent duplicate flight numbers
    while True:
        flight_number = collect_non_blank("Flight Number: ")
        if flight_number not in [flight.flight_number for flight in flights]: break
        print(f"{flight_number} is a duplicate flight number.")

    destination = collect_non_blank("Destination: ")
    departure_date = collect_non_blank("Departure Date: ")
    departure_time = collect_non_blank("Departure Time: ")
    capacity = collect_number("Flight Capacity: ")

    flight = Flight(
        flight_number=flight_number,
        destination=destination,
        departure_date=departure_date,
        departure_time=departure_time,
        capacity=capacity,
        seats_available=capacity # Seats available should default to capacity
    )
    flights.append(flight)
    save_flights(flights)

    print(f"Flight {flight.flight_number} added to flight schedule.")
    press_enter()

def view_flights(flights):
    prep_screen("Scheduled Flights")
    
    if not flights:
        print("No scheduled flight information available.")
    else:
        for flight in flights:
            flight.display()

    press_enter()
    
