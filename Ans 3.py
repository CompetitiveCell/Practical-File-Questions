import os

#Write_File Function
def write_file():
    main_file = open("main_file.txt",'w')
    choice = int(input("Enter how many lines you want to enter: "))
    for i in range(choice):
        line = input("Write any line : ")
        main_file.write(line)
        main_file.write('\n')
    main_file.close()
        

#Results function
def remove_a():
    main_file = open("main_file.txt",'r')
    secondary_file = open("secondary_file.txt",'w')
    letter_a = " "
    while letter_a:
        letter_a = main_file.readline()
        if 'a' not in letter_a:
            secondary_file.write(letter_a)
            secondary_file.write('\n')
        else:
            continue
            

#Displaying new file
def display_file():
    secondary_file = open("secondary_file.txt", 'r')
    lines = secondary_file.read()
    print(lines)
    secondary_file.close()


write_file()
remove_a()
display_file()
os.remove("main_file.txt")
os.rename("secondary_file.txt","main_file.txt")
