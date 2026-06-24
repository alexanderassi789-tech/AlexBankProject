balance = 20000
choice =(int(input("""

What would you like to do today? 
1. Check balance
2. deposit 
3. withdraw
4. Buy Airtime
5. Exit
""")))


Name = (input("What is your name? "))
Password = (int(input("What is your password? ")))

def Login(Name, Password):

   if Password == 1234:
      print(account)

      return(f"""
    LOGIN SUCCESSFUL
{Name}, Welcome to Alex bank PLC.
How can we help you today? """)

   else:
      return(f"Sorry {Name}, You have inputed Invalid creedentials" )
account = Login(Name, Password)
print(account)

def atm(account, choice, balance):
 
 if choice == 1:
    return(f"Your balance is {balance}")
 elif choice == 2:
        amount = (int(input("enter deposit amount... ")))
        balance += amount
        return(f"Your updated balance is N{balance}")
    
 elif choice == 3:
        withdraw = (int(input("how much would you like to withdraw? ")))
        balance -= withdraw
        if withdraw > balance:
             return(f"Insufficient balance!")
        
 if withdraw <= balance:
       return(f"withdraw succecful, your current balance is N{balance}")

 elif choice == 4:
          airtime = (int(input(
              """How much airtime would you like to purchase?  
           1. 4GB for N400
           2. 2GB for N500
           3. 1GB for N100
        
          """)))

          balance -= airtime
          return(f"Airtime purchase successful, your current balance is N{balance} ") 

 elif choice == 5:
    return("Thank you for banking with us, see you next time! ")

 else:
     return("Invalid input")


Multi_choice = atm(account, choice, balance)
print(Multi_choice)






