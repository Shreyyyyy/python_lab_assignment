class AirlineTicketBooking:
def __init__(self, passenger_name, destination, flight_number,␣
↪ticket_price, seat_number):
self.passenger_name = passenger_name
self.destination = destination
self.flight_number = flight_number
self.ticket_price = ticket_price
self.seat_number = seat_number
def display_ticket_info(self):
print("Passenger:", self.passenger_name)
print("Destination:", self.destination)
print("Flight Number:", self.flight_number)
print("Ticket Price:", self.ticket_price)
print("Seat Number:", self.seat_number)
def update_ticket_price(self, new_price):
self.ticket_price = new_price
print("Ticket price updated to:", self.ticket_price)
def verify_seat_availability(self):
if self.seat_number > 0:
print("Seat is available.")
else:
print("Seat is not available.")
# Inheritance
class BusinessClassTicket(AirlineTicketBooking):
def __init__(self, passenger_name, destination, flight_number,␣
↪ticket_price, seat_number, lounge_access):
super().__init__(passenger_name, destination, flight_number,␣
↪ticket_price, seat_number)
self.lounge_access = lounge_access
def display_ticket_info(self):
super().display_ticket_info()
1
print("Lounge Access:", self.lounge_access)
# Polymorphism
def print_ticket_details(ticket):
ticket.display_ticket_info()
# Creating objects
ticket1 = AirlineTicketBooking("Shrey", "New York", "UA123", 500, 25)
ticket2 = BusinessClassTicket("Oishi", "London", "BA456", 1500, 12, True)
print("---------------------------------------")
# Calling methods
ticket1.display_ticket_info()
ticket1.update_ticket_price(550)
ticket1.verify_seat_availability()
print("---------------------------------------")
ticket2.display_ticket_info()
ticket2.update_ticket_price(1600)
ticket2.verify_seat_availability()
print("---------------------------------------")
print("\nPolymorphism Example:")
tickets = [ticket1, ticket2]
for ticket in tickets:
print_ticket_details(ticket)
print("---------------------------------------")
