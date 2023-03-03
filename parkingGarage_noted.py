class parkingGarage():
    def __init__(self, ticket, p_space, c_ticket):
        self.tickets = ticket
        self.p_spaces = p_space
        self.c_tickets = c_ticket
    # def t_ticket(self):
    #     self.tickets.pop(ticket)
    #     self.p_spaces.pop()
    def t_ticket(self):
        self.tickets.pop(self)
        self.p_spaces.pop(p_space)
    def pf_parking(self, payment):
        self.payment = input(int("Please submit payment amount: "))
        if self.payment != 0:
            print("Your payment has been accepted. You have 15 minutes to leave.")
            self.c_ticket[paid] = True
        else:
            print("No payment has been received")
            parkingGarage(pf_parking)
    def l_garage(self):
        if self.c_tickets[0] == True:
            print("Thank you, have a nice day")
            self.p_spaces.append(1)
            self.tickets.append(1)
        else:
            X = input("Ticket has not been paid. Please submit payment amount: ")
            if x != 0:
                print("Thank you, have a nice day!")


def run():
    while True:
        resp = input("Take ticket, pay for parking, or leave garage?")
        
        if resp.lower() == "take ticket":
            parkingGarage.t_ticket()
        elif resp.lower() == "pay for parking":
            parkingGarage.pf_parking()
        elif resp.lower() == "leave garage":
            parkingGarage.l_garage()
            break

Carlson = parkingGarage([], [], {})
ticket = (1, 1, 1, 1, 1)
run()



