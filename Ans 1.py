file = open("HashTextFile.txt", "w")
file_data = []
choice = int(input("Enter how many lines to enter: "))

def write_file(choice):
    for i in range(choice):
        line = input("Write any line : ")
        file_data.append(line + '\n')
        file.writelines(file_data)
    file.close()

write_file(choice)

file = open("HashTextFile.txt", "r")
data = " "
while data:
    data = file.readline()
    for word in data.split():
        print(word, end = "#")

file.close()
