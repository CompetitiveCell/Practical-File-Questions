file = open("dictionary_file.txt", "w")

#Writing in the file
def write_file():
    choice = int(input("Enter how many lines you want to enter: "))
    for i in range(choice):
        line = input("Write any line : ")
        file.write(line)
        file.write('\n')
    file.close()

def file_dict():
    file = open("dictionary_file.txt", "r")
    data_dict = {}
    data = file.read()
    data = data.split()
    for i in data:
        word_count = data.count(i)
        data_dict[i] = word_count
    print(data_dict)

write_file()
file_dict()
