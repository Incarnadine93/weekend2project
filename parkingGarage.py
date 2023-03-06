class parkingGarage():
    def __init__(self):
        self.tickets = 10 #tickets available
        self.p_spaces = 10 #parking spaces available
        self.c_ticket = {"paid":False} #current ticket
    # def t_ticket(self):
    #     self.tickets.pop(ticket)
    #     self.p_spaces.pop()
    def t_ticket(self):
        self.tickets -= 1
        print(f"{self.tickets} tickets available")
        self.p_spaces -= 1
        print(f"{self.p_spaces} parking spaces available")
    def pf_parking(self):
        while True:
            payment = int(input("Please submit payment amount of $10: "))
            if payment == 10: #parking is 10 dollars
                print("Your payment has been accepted. You have 15 minutes to leave.")
                self.c_ticket["paid"] = True 
                break
            elif payment > 0 and payment < 10:
                print("Payment declined. Please submit proper payment amount")
                payment = 0
            elif payment == 0:
                print("No payment has been received")
    def l_garage(self):
        if self.c_ticket["paid"] == True:
            print("Thank you, have a nice day")
            self.p_spaces += 1
            print(f"{self.p_spaces} parking spaces available")
            self.tickets +=1
            print(f"{self.tickets} tickets available")
        else:
            while True:
                X = int(input("Ticket has not been paid. Please submit payment amount of $10: "))
                if X == 10:
                    print("Thank you, have a nice day!")
                    break
                elif X > 0 and X < 10:
                    print("Payment declined. Please submit proper payment amount")
                    X = 0
                else:
                    print("No payment has been received")


def run():
    while True:
        resp = input("Take ticket, pay for parking, or leave garage?")
        
        if resp.lower() == "take ticket":
            Carlson.t_ticket()
        elif resp.lower() == "pay for parking":
            Carlson.pf_parking()
        elif resp.lower() == "leave garage":
            Carlson.l_garage()
            break

Carlson = parkingGarage()
run()



