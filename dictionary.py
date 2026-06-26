# STUDENT MANAGEMENT SYSTEM
# This is version 2, trying to make it better....
choice = (int(input("""
1. Add Student 
2. View Students
3. Search Students
4. Update Student                   

Enter your choice: """)))
if choice == 1:

        name = (input("Enter Student name: ") .title())
        age = (int(input("Enter Student Age: ")))
        school = (input("Enter Student School: ").title())
        department = (input("Enter student department: ").title())
        level = (int(input("Enter student level: ")))

        student = {
                "name" : name,
                "age"  : age,
                "school" : school,
                "department" : department,
                "level" : level,
                }
        for key, value in student.items():
                print(key, ":", value)
                print("STUDENT ADDED SUCCESSFULY!")
else:
        print("Options doesnt work for now")
         
