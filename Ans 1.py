file = open("HashTextFile.txt", "w")

def write_file():
    file_data = []
    choice = int(input("Enter how many lines to enter: "))
    for i in range(choice):
        line = input("Write any line : ")
        file_data.append(line + '\n')
    file.writelines(file_data)

write_file()

file = open("HashTextFile.txt", "r")
data = " "
data = file.read()
for word in data.split():
    print(word, end = "#")

file.close()
