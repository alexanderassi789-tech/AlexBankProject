# BUILDING AN ATM MACHINE

balance = 20000
# here we are giving it the balance which it can use to perform

# HERE WE CREATED THE USER CHOICE TO SCAN THROUGH OPTIONS 
choice = (int(input("""
Welcome to Alex bank PLC, How can we help you today?              
1. Check balance
2. Deposit
3. Withdraw 
4. Purchase Airtime
5. Exit                     """)))

# HERE WE ARE CREATING THE FUNCTIONS
def alex_bank(balance , choice):
    if choice == 1:
        return (f"Your balance is: N{balance}")
    elif choice == 2:
        deposit = (int(input("How much would you like to deposit? ")))
        print(deposit)
        return(f"Your new balance is: N{balance + deposit}")
    elif choice == 3:
        withdraw = (int(input("How much would you like to withdraw? ")))
        print(withdraw)
        if withdraw > balance:
            return("Insufficient balance! ")
        if withdraw <= balance:
            return (f"Withdraw successful, Your new balance is: N{balance - withdraw}")
    elif choice == 4:
        airtime = (int(input("""How much airtime would you like to purchase?
        1. 1GB for N1,000
        2. 2GB for 2,0000
        3. 5GB for 3,000
                       """)))
        print(airtime)
        if airtime == 1:
            return(f"Airtime purchase  successful!, your current balance is: {balance - airtime} ")
        if airtime == 2: 
            return(f"Airtime purchase was successful!, your current balance is: {balance - airtime} ")
        if airtime == 3:
            return(f"Airtime purchase was successful!, your current balance is: {balance - airtime} ")
        else:
            return("Invalid option")
    elif choice == 5:
        return("Thank you for banking with us")

ATM = alex_bank(balance, choice)
print(ATM) 
                 
    




