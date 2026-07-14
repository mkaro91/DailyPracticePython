from Services import *
from Classes import *

def main():
    flights = load_flights()
    passengers = load_passengers()
    reservations = load_reservations()

    while True:
        prep_screen("Airline Reservation System")
        print("\n1. Add Flight")
        print("2. View Flights")
        print("3. Register Passenger")
        print("4. View Passengers")
        print("5. Book Flight")
        print("6. Cancel Reservation")
        print("7. View Reservations")
        print("8. Search")
        print("0. Exit")

        choice = menu_choice()
        match choice:
            case "0": break
            case "1": add_flight(flights)
            case "2": view_flights(flights)
            case "3": register_passenger(passengers)
            case "4": view_passengers(passengers)
            case "5": book_flight(flights, passengers, reservations)
            case "6": cancel_reservation(reservations, flights)
            case "7": view_reservations(reservations, flights, passengers)
            case "8": search_menu(flights, passengers, reservations)

            case _:
                print("Invalid choice.")
                press_enter()

if __name__ == "__main__":
    main()