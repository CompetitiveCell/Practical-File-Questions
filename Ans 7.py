from pickle import *

def write_file():
    student_data = {}
    file = open("student_record.dat", "wb")
    choice = int(input("How many records you want to enter : "))
    for i in range(choice):
        rno = int(input("Enter Roll Number : "))
        name = input("Enter Student Name : ")
        student_data[rno] = name
        dump(student_data, file)
    
#Searching in the file
def search_file():
    file = open("student_record.dat", "rb")
    roll_number = int(input("Enter what roll number to search : "))
    found = False
    try:
        while True:
            data = load(file)
            for i in data:                
                if i == roll_number:
                    records = data.get(roll_number)
                    found = True
    except EOFError:
        if found == False:
            print("No record found in the file")
        else:
            print("Name of roll number",roll_number,"is",records)
            print("Searching Successful")

write_file()
search_file()
