from Classes.reservation import Reservation

from helpers import *

from Services.flight_service import find_flight_by_number, save_flights
from Services.passenger_service import find_passenger_by_passport

import os
import json

RESERVATION_SAVE = "data/reservations.json"

def save_reservations(reservations):
    os.makedirs("data", exist_ok=True)
    data = [reservation.to_dict() for reservation in reservations]

    with open(RESERVATION_SAVE, 'w') as f:
        json.dump(data, f, indent=2)

def load_reservations():
    try:
        with open(RESERVATION_SAVE, 'r') as f:
            return [Reservation.from_dict(r) for r in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def find_reservation_by_id(reservations, id):
    for reservation in reservations:
        if reservation.id == id.upper():
            return reservation
    return None

def check_double_booking(reservations, passport_number, flight_number):
    for reservation in reservations:
        if reservation.passport_number == passport_number and reservation.flight_number == flight_number:
            return True
    return False

def book_flight(flights, passengers, reservations):
    passport_number = collect_non_blank("Enter Passenger's Passport Number: ").upper()
    passenger = find_passenger_by_passport(passengers, passport_number)
    if not passenger:
        print(f"Please register passport number '{passport_number}' before continuing.")
        press_enter()
        return
    
    flight_number = collect_non_blank("Enter Flight Number: ").upper()
    flight = find_flight_by_number(flights, flight_number)
    if not flight:
        print("No flight with matching flight number found.")
        press_enter()
        return
    
    if flight.is_full:
        print("Flight is already at maximum capacity.")
        press_enter()
        return
    
    if check_double_booking(reservations, passport_number, flight_number):
        print(f"{passenger.name} is already booked for Flight {flight.flight_number}.")
        press_enter()
        return
    
    if not reservations:
        id = "RES-0001"
    else:
        new_id = str(int(reservations[-1].id.split("-")) + 1)
        zeros = '0' * (4 - len(new_id))
        id = f"RES-{zeros}{new_id}"

    reservation = Reservation(
        reservation_id = id,
        flight_number = flight_number,
        passport_number = passport_number,
        seat_number = flight.generate_seat_number()
    )
    reservations.append(reservation)
    save_reservations(reservations)
    print(f"Reservation {reservation.id} completed.")

    flight.seats_available -= 1
    save_flights(flights)
    press_enter()

def cancel_reservation(reservations, flights):
    prep_screen("Cancel Reservation")
    id = collect_non_blank("Enter Reservation ID: ")
    reservation = find_reservation_by_id(reservations, id)
    if not reservation:
        print("no reservation with matching ID located.")
        press_enter()
        return
    reservations.remove(reservation)
    flight = find_flight_by_number(flights, reservation.flight_number)
    flight.seats_available += 1
    print(f"Reservation {reservation.id} removed from reservations.")
    save_reservations(reservations)
    save_flights(flights)
    press_enter()

def view_reservations(reservations, flights, passengers):
    prep_screen("Reservations")

    if not reservations:
        print("No reservations have been made.")
    else:
        for reservation in reservations:
            reservation.display(flights, passengers)
    
    press_enter()