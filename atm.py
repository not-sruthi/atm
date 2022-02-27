class Atm (object):
    def __init__(self, cardNo, pinNo, bal):
        self.cardNo = input("Enter your card number: ")
        self.pinNo = input("Enter your PIN number: ")
        self.bal = int(input("How much money is in your account? "))

    def balance(self):
        card = input("Enter your card number. ")
        if (card==self.cardNo):
            print()
            print("Your balance is", self.bal)
            return(' ')
        else:
            return("Your card number is incorrect.")
            
    def withdraw(self):
        pin = input("Enter your pin. ")
        if (pin==self.pinNo):
            amount = int(input("How much do you want to withdraw? "))
            if (amount<=self.bal):
                self.bal = self.bal - amount

                print()
                print("You have withdrawn", amount , "successfully.")
                print("Your balance is" , self.bal)
                return(' ')
            else:
                return("You do not have that much money.")
        else:
            return("Your PIN number is incorrect.")

    def deposit(self):
        card = input("Enter your card number. ")
        if (card==self.cardNo):
            amount = int(input("How much do you want to deposit? "))
            self.bal = self.bal + amount

            print()
            print("You have deposited", amount , "successfully.")
            print("Your balance is" , self.bal)
            return(' ')
        else:
            return("Your PIN number is incorrect.")


run = Atm(1,1,10000)

isRunning = 'y'

while (isRunning == 'y'):
    print()
    print("Select an option.")
    choice = input(" Press 0 to cancel. \n Press 1 to check your balance. \n Press 2 to withdraw cash. \n Press 3 to deposit cash. ")
    print()
    if (choice == '0'):
        print("Thank you!")
        isRunning = 'n'
    elif (choice == '1'):
        print(run.balance())
    elif (choice == '2'):
        print(run.withdraw())
    elif (choice == '3'):
        print(run.deposit())
    else:
        print("Input not recognised, please try again.")
        print()