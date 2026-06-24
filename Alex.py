print("Hello world")
print("My name is Alexander")
print("I am learning python")
# VARIABLES: Used to store items inside a word or an object 
Name = "Alexander"
# Now we have stored Alexander inside the variable [Name]
print(Name)
# We can also store numbers inside variabes
Age = 18
print(Age)
# Lets make out some variabes and Construct a sentence
Name = "Alexander"
Age = 18
School = "UNN"
Residence = "Nsukka"

print("My name is")

print("Hello")  # STRING: They are TEXT inside quotes "", 
print(18)  # INTEGERS: They are whole numbers 
print(1.3)  # FLOAT: They are decimals

# ARITHEMETIC OPERATION: Python Maths... 
print(2+3)# ADDITION
print(10-4)# SUBTRACTION
print(5*3)# MULTIPLICATION
print(5/2)# DIVISION

# USING VARIABES IN MATHS 
ant = 18
ball = 2
print(ant + ball) # We got 20 as our answer
# Another example
age = 34
print(age + 66) #We got 100 as our answer
print(age * ball)
# USER INPUT: It lets the user type/ input something 
print("HIIII")

name= input("How old are you? ")
print("you are", name)
car= input("Welcome to Alex Car Auto, what do you want? ")
print("Sorry, we cant sell a", car) 

Name = input("What is your name? ")
print("Hello", Name)
Age = input("How old are you? ")
print("you are", Age)
School = input("What school do you attend? ")
print(School, "is a popular university" )

print(5>2)

age= 18
if age>=18:
    print("You can vote")

age = int(input("How old are you? "))

if age>= 18:
 print("you are an adult" )
else:
 print("You are a child")

Score= int(input("What was your exam score? "))
if Score>=80:
   print("Congratulations you passed, see you in next class")
else:
   print("You failed, you will have to repeat this class")

Race= input("What is your colour? ")
if Race== "white":
  print("You are welcome")
else:
  print("Sorry, We are not accepting right now")

Score=int(input("What was your test score? "))
if Score>= 70:
  print("A")
elif Score>=60:
  print("B")
elif Score>=50:
  print("C")
elif Score>=40:
  print("P")
else:
  print("F")

# LOGICAL OPERATORS: AND, OR & NOT
# To Write an AND function
age= int(input("Welcome to the polling unit, How old are you? "))
citizen = input("Are you a citizen of this country? ")
if age>=18 and citizen == "yes":
  print("You can vote")
elif age>=17 and citizen == "yes":
  print("Just one more year and you can vote")
else:
  print("You cant vote because you are not of age")

# To write an OR function
Department = input("What department are you? ")
Faculty = input("What faculty are you in? ")
if Department == "Computer Science" or Faculty == "Phyical Science":
  print("Since Youre in computer science welcome")
else:
  print("Sorry youre not with us, We cant welcome you.")

# LOOPS: A loop allow python to repeat action
for A in range(3):
  print(A)
 
count = 1
while count <= 6:
  print(count)
  count += 1 

fruits = ["Apple", "Banana", "Cashew"]
Shop =input("Welcome to alex store, What fruit would you like to buy? ")
if Shop in fruits:
  print(f"You order for {Shop}is available")
else:
  print(f"We dont have {Shop} sorry")


user_name= input("Please input your user_name ")
password = int(input("what is your password? "))
if user_name == "Alexander Assi" and password >= 1234:
  print(f"Welcome", {user_name} )
else:
  print("Invalid login session")
 
Name = input("What is your name? ")
Age = int(input("How old are you? "))
if Age>= 18:
  print(f"{Name}, Since you are {Age}, You are an adult!")
elif Age >=13:
  print(f"{Name}, since you are {Age}, You are a teenager!")
else:
  print(f"{Name}, You are a child!") 

