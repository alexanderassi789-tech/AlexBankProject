balance = 20000
choice =(int(input("""                   
1. Check Balance
2. Deposit
3. Withdraw
4. Buy Airtime
5. Exit                                                                          
Enter your option: """)))

def ATM(choice, balance):
    if choice == 1:
        return(f"Your balance is: N{balance}")
    elif choice == 2:
        deposit = (int(input("How much would you like to deposit? ")))
        balance += deposit
        return(f"Deposit Successful!, Your new balance is: N{balance}")
    elif choice == 3:
        withdraw = (int(input("How much would you like to withdraw? ")))
        if withdraw > balance:
            return("Insufficient balance!")
        elif balance >= withdraw:
             balance -= withdraw
             return(f"Withdraw Successful! Your current balance is: N{balance}")
    elif choice == 4:
        airtime = (int(input("""
               How much airtime would you like to purchase?
               1. 4GB for 4,000
               2. 2GB for 2,000
               3. 1GB for 1,000 
                Enter an option: """)))
        if airtime == 1:
            balance -= 4000
            return(f"Airtime purchase of 4GB was successful, Your new balance is: N{balance}")
        elif airtime == 2:
            balance -= 2000
            return(f"Airtime purchase of 2GB was successful, Your new balance is: N{balance}")
        elif airtime == 3:
            balance -= 1000
            return(f"Airtime purchase of 1GB was successful, Your new balance is: N{balance}") 
        else:
            return("Invalid Option")
    elif choice == 5:
        return("Thank you for banking with us")
    else:
        return("Invalid Option")

Login = ATM(choice, balance)
print(Login)


























