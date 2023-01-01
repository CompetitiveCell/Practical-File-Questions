#Writing in the file
def write_file():
    file = open("swap_case.txt", "w")
    choice = int(input("How many lines you want to enter : "))
    for i in range(choice):
        lines = input("Enter any line : ")
        file.write(lines)
        file.write("\n")

def swap_case():
    file = open("swap_case.txt", "r")
    temporary_file = open("tempo_swap_case.txt", "w")
    data_list = []
    data = file.read()
    data = data.swapcase()
    temporary_file.write(data)
    
def display_file():
    main_file = open("swap_case.txt","r")
    tempo_file = open("tempo_swap_case.txt","r")
    line = main_file.read()
    print("Main File : ")
    print(line)
    lines = tempo_file.read()
    print("Temp File : ")
    print(lines)
    
write_file()
swap_case()
display_file()
