# CREATING A STUDENT PROFILE MANGEMENT SYSTEM
# It takes student information ans stores them in a dictionary

name = (input("what is your name? ".title()))
age = (int(input("How old are you? ".title())))
school = (input("What schhol do you attend? ".title()))
department = (input("Enter your department: ".title()))
level = (int(input("enter your level: ".title())))

student_profile = {
"name" : name,
"age" : age,
"school" : school,
"department" : department,
"level" : level,
                  }

print ("=" * 30)
print("STUDENT PROFILE")
print("=" * 30)
for key, value in student_profile.items():
    print(key, ":", value)




