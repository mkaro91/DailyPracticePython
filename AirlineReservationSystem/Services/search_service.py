from helpers import *

from Services.flight_service import find_flight_by_number
from Services.passenger_service import find_passenger_by_passport
from Services.reservation_service import find_reservation_by_id

def search_menu(flights, passengers, reservations):
    while True:
        prep_screen("Search")

        print("\nSearch Target:")
        print("1. Search Flights")
        print("2. Search Passengers")
        print("3. Search Reservations")
        print("0. Return to Main Menu")

        choice = menu_choice()
        match choice:
            case "0": return

            case "1":
                flight_number = collect_non_blank("Enter Flight Number: ").upper()
                
                flight = find_flight_by_number(flights, flight_number)
                if not flight:
                    print("No flight with matching flight number found.")
                else:
                    flight.display()
                
                press_enter()
            
            case "2": 
                passport_number = collect_non_blank("Enter Passport Number: ").upper()

                passenger = find_passenger_by_passport(passengers, passport_number)
                if not passenger:
                    print("No passenger with matching passport number found.")
                else:
                    passenger.display()
                
                press_enter()
            
            case "3":
                reservation_id = collect_non_blank("Enter Reservation ID: ").upper()

                reservation = find_reservation_by_id(reservations, reservation_id)
                if not reservation:
                    print("No reservation with matching ID found.")
                else:
                    reservation.display()
                
                press_enter()
            
            case _:
                print("Invalid choice.")
                press_enter()