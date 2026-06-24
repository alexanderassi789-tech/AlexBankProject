Name = (input("What is your name? "))
Password = (int(input("What is your password? ")))

def Login(Name, Password):
   if Password == 1234:
      return(f"""
    LOGIN SUCCESSFUL
{Name}, Welcome to Alex bank PLC.
How can we help you today? """)
   
   else:
      return(f"Sorry {Name}, You have inputed Invalid creedentials" )

print(Login(Name, Password))

