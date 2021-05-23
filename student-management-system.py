# Project: Student Management System
# Version: 3.0
#Date: May 9, 2021

print("-"*25, "Welcome to Student Management System (SMS, ver 3.0)", "-"*25)

# Students list
# use dictionary to represent student

s1 = {'name': 'Jack',
'age': 13,
'gender': 'Male',
'address': 'San Diego'}

s2 = {'name': 'Jenny',
'age': 11,
'gender': 'Female',
'address': 'San Diego'}

students = [s1, s2]
# print(students[0])
# print(students[1])

while True:
    # Menu
    print("Please choose from the following options:")
    print("\t1. Display Students")    # R - reading
    print("\t2. Add New Student")     # C - creation
    print("\t3. Delete Student")      # D - deletion
    print("\t4. Modify Student Info") # U - updating
    print("\t5. Exit System")         # E - Exiting

    user_input = input("Please choose [1-5]: ")
    # print(f"user_input is {user_input}")
    print("-" * 80)

    if user_input == "1":
        print(f"No.\t{'Name':10s}\t{'Age':5s}\t{'Gender':8s}\tLocation")
        print("-"*80)
        no = 1
        for stu in students:
            print(str(no) + "\t" + f"{stu['name']:10s}" + "\t" + f"{str(stu['age']):5s}" + "\t" + f"{stu['gender']:8s}" + "\t" + stu['address'])
            no += 1
        
    elif user_input == "2":
        # print("Add new student")
        stu_name = input("Please input student name: ")
        stu_age = int(input("Please input student's age: "))
        stu_gender = input("Please input student's gender: ")
        stu_loc = input("Please input student's location: ")

        new_stu = dict(name=stu_name, age=stu_age, gender=stu_gender, address=stu_loc)
        print("-"*80)
        print(f"{stu_name} will be added to the students database...")

        user_confirm = input("Do you confirm the operation above? [y/n]")
        if user_confirm == "y":
            students.append(new_stu)
            print(f"{stu_name} has been added to students database...")
        else:
            print("You cancelled the operation.")

    elif user_input == "3":
        # print("Delete student")
        del_stu_no = len(students)

        if 0 < deal_stu_no <= len(students):

            del_stu_no = int(input("Please input the no. of the student you want to delete: "))

            if 0 < del_stu_no <= len(students):

                del_stu_confirm = input(f"Dro you confirm to delete the student of no. {del_stu_no}? [y/n]")
                if del_stu_confirm == "y":
                    students.pop(del_stu_no - 1)
                    print(f"The student of no. {del_stu_no} has been deleted.")
                else:
                    print("You canceled the operation.")

            else:
                print("Please input a valid student no.")
        elif user_input == "4":
            print("Modify a student's info")
            edit_student_no = int (input("Please input the no. of the student you want to modify: "))

            if 0 < edit_stu_no <= len(students):
                edit_stu_confirm = input(f"Do you confirm to modify the student of no. {edit_stu_no}? [y/n]")
                if edit_stu_confirm == "y":
                    new_name = input("Please input the student's new name (press 'n' to skip): ")
                    if new_name != 'n':
                        new_age = int(new_age)
                        students[edit_stu_no - 1]['age'] = new_age

                    new_loc = input("Please input the student's new location (press 'n' to skip): ")
                    if new_loc != 'n':
                        students[edit_stu_no - 1]['address'] = new_loc
                    print(f"Student of no. {edit_stu_no} has been updated.")
                else:
                    print("You cancelled the operation.")

            else:
                print("You cancelled the operation.")

        else:
            print("Please input a valid student no.")



    elif user_input == "5":
        print("Thank you for using SMS! See you later...")
        break
    else:
        print("Please input a valid option...")

    print("-" * 80)    
