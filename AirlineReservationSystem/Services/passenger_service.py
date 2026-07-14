import os
import json

from helpers import *

from Classes.passenger import Passenger

PASSENGER_SAVE = "data/passengers.json"

def save_passengers(passengers):
    os.makedirs('data', exist_ok=True)
    data = [passenger.to_dict() for passenger in passengers]

    with open(PASSENGER_SAVE, "w") as f:
        json.dump(data, f, indent=2)

def load_passengers():
    try:
        with open(PASSENGER_SAVE, 'r') as f:
            return [Passenger.from_dict(passenger) for passenger in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def find_passenger_by_passport(passengers, passport_number):
    for passenger in passengers:
        if passenger.passport_number == passport_number:
            return passenger
    return None

def register_passenger(passengers):
    prep_screen("Register Passenger")

    name = collect_non_blank("Passenger Name: ")
    age = collect_number("Passenger Age: ")

    while True:
        passport_number = collect_non_blank("Passport Number: ")
        if passport_number not in [passenger.passport_number for passenger in passengers]: break
        print(f"Passport Number {passport_number} is already registered.")

    passenger = Passenger(
        name=name,
        passport_number=passport_number,
        age=age
    )
    passengers.append(passenger)
    save_passengers(passengers)

    print(f"{passenger.name} registered!")
    press_enter()

def view_passengers(passengers):
    prep_screen("Passengers")

    if not passengers:
        print("No passenger information available.")
    else:
        for passenger in passengers:
            passenger.display()
    
    press_enter()