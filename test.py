class Truck():
    def __init__(self, wheels, gallons, items):
        self.wheels = wheels
        self.gas_tank = gallons
        self.items = items
        
    def showItems(self):
        print("Let's look in the back and see what there is . . .")
        for i in self.items:
            print(i)
            
    # def showTank(self):
    #     print(f"you've got {self.gas_tank} gallons of gas")
        
    def addItems(self):
        item = input("What are you throwing in the back?")
        self.items.append(item)      

def run():
    while True:
        resp = input("What to do  a for add items, s for show, q for quit")
        
        if resp.lower() == "q":
            dodge.showItems()
            print("thanks for spending time with the truck game")
            break
        elif resp.lower() == "a":
            dodge.addItems()
        elif resp.lower() == "s":
            dodge.showItems()

# See Above
dodge = Truck(4, 10, [])


run()