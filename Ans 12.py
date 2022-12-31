import csv

def write_file():
    global choice
    file = open("user_data.csv", "w")
    file_writer = csv.writer(file)
    file_writer.writerow(["User-Id","Password"])
    choice = int(input("How many records you want to enter : "))
    for i in range(choice):
        print("User-ID for User", i+1)
        user_id = input("Enter your user-id : ")
        password = input("Enter your password : ")
        data = [user_id, password]
        file_writer.writerow(data)

def search_file():
    file = open("user_data.csv", "r", newline = '\r\n')
    file_reader = csv.reader(file)
    search = input("Enter username whose password to be searched : ")
    for i in range(choice):
        for i in file_reader:
            if i[0] == search:
                print("Password of",search,"is",i[1])
    
write_file()
search_file()
