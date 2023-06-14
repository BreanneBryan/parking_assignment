class Garage():
    """
    Class to simulate a parking garage. When instantiating, one must provide
    the total number of spaces in parking garage.
    """
    def __init__(self,total_spaces:int):
        self.total_spaces = total_spaces
        self.open_spots = total_spaces
        self.visitors = dict()
        self.tickets = list()

    def currentVisitors(self):
        """
        Method to print out the current visitors and their payment status
        """
        if len(self.visitors) == 0:
            print("There are no visitors.")
            return
        length = 7
        for visitor in self.visitors.keys(): 
            length = max(length, len(visitor))
        
        print("visitors".ljust(length, " ") + "   -   " + "paid ticket")
        print()

        for visitor, payment_status in self.visitors.items():
            x = visitor.ljust(length, " ") + "   -   " + str(payment_status)
            print(x)
        return

    def takeTicket(self,visitor:str,show_text:bool=True):
        """
        Method to add a visitor to the parking garage. One must provide the visitor's name
        when doing this. There is also an option to surpress the output text when a visitor
        successfully enters the garage
        """
        if self.open_spots == 0:
            print(f"Sorry {visitor}, no parking space-available")
            return
        
        if not isinstance(visitor,str) or not visitor:
            print("Visitor's name must be a non-empty string")
            return
        
        visitor = visitor.strip().lower()

        if visitor in self.visitors:
            print("Sorry, someone is already in here with that name, so we can't let you in. If you must come in, please use a nickname or add numbers to your name")
            return
        
        self.visitors[visitor] = False
        self.open_spots -= 1
        if show_text:
            print(f"Welcome to the garage {visitor}, enjoy your time!")
            print("Make sure to pay for your ticket with 'pay' command before you leave")
        return

    def payTicket(self, visitor:str):
        """
        Method to pay for a visitors parking ticket. One must provide the visitor's name. 
        This must be done prior to leaving garage.
        """
        if not isinstance(visitor,str) or not visitor:
            print("Visitor's name must be a non-empty string")
            return

        visitor = visitor.strip().lower()
        if visitor not in self.visitors:
            print("Hey you don't need to pay!")
            return

        if self.visitors[visitor] == True:
            print("You have already paid. Feel free to leave whenever!")
            return
        
        # times refused to pay
        times_refused = -1
        while True:
            times_refused += 1
            print('Please type $5 to pay your ticket!')
            pay = input().strip()

            if pay != "$5":
                print("You have entered the incorrect amount.")
                        
            print("Thank you for the payment! When ready, please leave with the 'leave' command ")
            break
        
        self.visitors[visitor] = True

        # Add name to ticket list to store record of their paid ticket
        ticket_val = 5.0
        self.tickets.append((visitor,ticket_val)) 

        return

    def leaveGarage(self, visitor:str):
        """
        Method for vistor to leave garage. One must provide the visitor's name. 
        """
        if not isinstance(visitor,str) or not visitor:
            print("Visitor's name must be a non-empty string")
            return
        
        visitor = visitor.strip().lower()
        if visitor not in self.visitors:
            print("You never got a ticket how are you trying to leave?")
            return

        
        if self.visitors[visitor] == False:
            print("You have not payed yet please pay with the 'pay' command")
            return


        print(f"Thank you for visiting our garage {visitor} come again soon!")
        
        del self.visitors[visitor]
        self.open_spots += 1
        return
    
    def moneyMade(self):
        """
        Method to print the amount of money made since instantiating the garage.
        """
        total = 0
        for _,val in self.tickets:
            total += val
        print("$"+str(int(total)))
        return total
    
    
def create_garage():
    def print_instructions():
        print("'enter'")
        print("command to enter garage")
        print("'pay'")
        print("pay for ticket, must be done after entering")
        print("'leave'")
        print("leave garage")
        print("'commands'")
        print("repeats these commands")
        return
    

    print("Thanks for opening the garage!")
    while True:
        print("How many parking spots do you want in your garage?")
        spots = input()
        try:
            spots = int(spots)
        except:
            print("Please enter an integer above zero")
            continue

        if spots <= 0:
            print("Please enter an integer above zero")
            continue

        break

    garage = Garage(spots)
    print("Welcome to this garage")
    print("The following commands are ones for the general public....")
    print_instructions()

    print("enter any character to print the garage owner only commands")
    input()

    print("the following commands are just for the garage owner....")
    print()
    print("'list current visitors'")
    print("shows all current visitors in garage and their payment status")
    print()
    print("'revenue'")
    print("prints out total renvue made thus far")
    print()
    print("'shut down'")
    print("shuts down garage")
    print()

    print("enter any character to print a bunch of empty lines and hide manager commands")
    input()
    for _ in range(50):
        print()
    
    while True:
        print()
        print("What would you like to do?")
        response = input().strip().lower()
        
        if response == "enter":
            print("What is your name?")
            name = input().strip().lower()
            garage.takeTicket(name)

        elif response == "pay":
            print("What is your name?")
            name = input().strip().lower()
            garage.payTicket(name)

        elif response == "leave":
            print("What is your name")
            name = input().strip().lower()
            garage.leaveGarage(name)

        elif response == "list current visitors":
            garage.currentVisitors()
        
        elif response == "revenue":
            garage.moneyMade()

        elif response == "shut down":
            print("Garage is being shut down")
            break
        
        elif response == "commands":
            print_instructions()
        
        else:
            print("That was not a valid command. Please type 'commands' to see a list of valid commands")
        
    return


if __name__ == "__main__":
    create_garage()