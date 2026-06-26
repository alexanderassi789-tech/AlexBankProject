# BUILDING AN ATM MACHINE

balance = 20000
# here we are giving it the balance which it can use to perform

# HERE WE CREATED THE USER CHOICE TO SCAN THROUGH OPTIONS 
Login = (input("What is your name? "))
password = (int(input("Insert your PIN: ")))
choice = (int(input("""
Welcome to Alex bank PLC, How can we help you today?              
1. Check balance
2. Deposit
3. Withdraw 
4. Purchase Airtime
5. Transfer money
6. Exit                     """)))

# HERE WE ARE CREATING THE FUNCTIONS
def alex_bank(Login, password, balance , choice,):
    if Login == "alexander" and password == 1:
        return("Login Successful")
    
    if choice == 1:
        return (f"Your balance is: N{balance}")
    elif choice == 2:
        deposit = (int(input("How much would you like to deposit? ")))
        balance += deposit
        return(f"Your new balance is: N{balance}")
    elif choice == 3:
        withdraw = (int(input("How much would you like to withdraw? ")))
        
        if withdraw > balance:
            return("Insufficient balance! ")   
        
        withdraw <= balance
        balance -= withdraw
        return (f"Withdraw successful, Your new balance is: N{balance}")
    elif choice == 4:
        airtime = (int(input("""How much airtime would you like to purchase?
        1. 1GB for 1,000
        2. 2GB for 2,0000
        3. 5GB for 3,000
                       """)))
        if airtime == 1:
            return(f"Airtime purchase  successful!, your current balance is: N{balance - 1000 } ")
        elif airtime == 2: 
            return(f"Airtime purchase was successful!, your current balance is: N{balance - 2000} ")
        elif airtime == 3:
            return(f"Airtime purchase was successful!, your current balance is: N{balance - 3000} ")
        else:
            return("Invalid option")
    elif choice == 5:
        Name = (input("Enter the name of recipiet: "))
        Bank = (input("What bank would you like to transfer to? "))
        Transfer = (int(input("How much would you like to transfer? ")))
        if Transfer > balance:
            return ("Insufficient balance! ")
        balance -= Transfer
        return(f"""
      TRANSACTION SUCCESSFUL!
      NAME: {Name}
      BANK: {Bank}
      AMOUNT: N{Transfer}
       Current Balance: N{balance}   
        
        
               
               
               """)
        
    elif choice == 6:
        return("Thank you for banking with us")
    else:
        return("Invalid  Option")

ATM = alex_bank(Login, password, balance, choice)

if password == 1234 and Login == "Alexander":
    print(ATM)
else:
    print("invalid Credentials")
                    



