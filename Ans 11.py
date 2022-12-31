
import pickle
import os
import sys

def add():
    st = {}
    file = open("school.dat", "ab")
    ch ="y"
    while ch in "yY":
        adno = int(input("Emter admission number : "))
        name = input("Enter Name : ")
        age = int(input("enter Age: "))
        engmarks = float(input("English marks : "))
        sciencemarks = float(input("Science marks : "))
        mathsmarks = float(input("Maths marks : "))
        st["admno"] = adno
        st["name"] = name
        st["age"] = age
        st["english"] = engmarks
        st["science"] = sciencemarks
        st["maths"] = mathsmarks
        pickle.dump(st, file)
        ch = input("Do you wish to enter more records press Y or y: ")
    file.close()

def read():
    st = {}
    file = open("school.dat", "rb")
    try:
        while True:
            st = pickle.load(file)
            print(st)
    except EOFError:
        print("All records displayed")
    file.close()

def search():
    st = {}
    flag = 0
    file = open("school.dat", "rb")
    name = input("Name to be searched: ")
    try:
        while True:
            st=pickle.load(file)
            if st["name"]==name:
                print(st)
                flag=1
    except EOFError:
        if flag == 0:
            print("Record not found")
    file.close()

def update():
    st = {}
    flag = 0
    file = open("school.dat", "rb+")
    ad = int(input("Enter admissison number whose marks is to be updated: "))
    M = float(input("How much marks to be updated in Maths: "))
    try:
        while True:
            pos = file.tell()
            st = pickle.load(file)
            if st["admno"] == ad:
                st["maths"] += M
                file.seek(pos)
                pickle.dump(st, file)
                print("Record Updated")
                flag = 1
    except EOFError:
        if flag == 0:
            print("Record not found")
    file.close()
    read()
def delete():
    st = ()
    flag = 0
    file = open("school.dat", "rb+")
    file1 = open("school1.dat", "wb+")
    ad_number = int(input("Enter admission number whose record to be deleted: "))
    try:
        while True:
            s = pickle.load(file)
            if st["admno"] != ad_number:
                pickle.dump(st, file1)
                flag = 1
            else:
                flag = 0
    except EOFError:
        if flag ==1:
            print("Record to be deleted not found")
    file.close()
    file1.close()
    os.remove("school.dat")
    os.rename("school1.dat", "school.dat")
    print("The file after deletion -----------------------")
    print()
    st = {}
    with open("school.dat", "rb") as file:
        try:
            st = pickle.load(file)
            print(st)
        except EOFError:
            file.close()

ch = 'y'
while ch == 'y':
    print("1 for Add Record")
    print("2 for Display all records")
    print("3 for Search a record")
    print("4 for Update a record")
    print("5 for Delete a record")
    print("0 for exit")
    c = int(input("Enter Choice: "))
    if c == 1:
        add()
    elif c == 2:
        read()
    elif c == 3:
        search()
    elif c == 4:
        update()
    elif c == 5:
        delete()
    elif c == 0:
        exit()
    else:
        print("Wrong Choice")

    ch = input("Enter y for menu otherwise enter any character")
