from pickle import *
import os

#Writing into the file
def write_file():
    employee_data = {}
    file = open("employee_data.dat", "wb")
    choice = int(input("How many records to enter : "))
    for i in range(choice):
        employee_no = int(input("Enter Employee Number : "))
        name = input("Enter Employee Name : ")
        salary = int(input("Enter Employee Salary : "))
        employee_data["Employee Number"] = employee_no
        employee_data["Name"] = name
        employee_data["Salary"] = salary
        dump(employee_data, file)

def salary_compare():
    data = {}
    found = False
    main_file = open("employee_data.dat", "rb")
    second_file = open("new_employee_data.dat", "wb")
    try:
        while True:
            data = load(main_file)
            if data["Salary"] > 25000:
                dump(data, second_file)
                found = True
            else:
                found = False
    except EOFError:
        if found == False:
            print("Record to be deleted not found")
        else:
            print("Record deleted")
            
write_file()
salary_compare()
os.remove("employee_data.dat")
os.rename("new_employee_data.dat", "employee_data.dat")
