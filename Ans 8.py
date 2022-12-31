from pickle import *

def write_file():
    student_data = {}
    file = open("student_data.dat", "wb")
    choice = int(input("How many records to enter : "))
    for i in range(choice):
        rno = int(input("Enter Roll Number : "))
        name = input("Enter Name : ")
        marks = int(input("Enter Marks : "))
        student_data["Roll Number"] = rno
        student_data["Name"] = name
        student_data["Marks"] = marks
        dump(student_data, file)

def update_marks():
    data = {}
    flag = 0
    file = open("student_data.dat", "rb+")
    roll_no = int(input("Enter Roll Number whose marks to be updated : "))
    new_marks = int(input("Enter the new marks : "))
    try:
        while True:
            position = file.tell()
            data = load(file)
            if data["Roll Number"] == roll_no:
                data["Marks"] = new_marks
                file.seek(position)
                dump(data, file)
                print("Marks Updated")
                flag = 1
    except EOFError:
        if flag == 0:
            print("Record not found")

write_file()
update_marks()
