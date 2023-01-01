file = open("letter_file.txt", "w")

#List definition
vowels = ['a','A','e','E','i','I','o','O','u','U']
consonants = ['b','B','c','C','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N',
              'p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x','X','y','Y','z','Z']

#Write_File Function
def write_file():
    choice = int(input("Enter how many lines you want to enter: "))
    for i in range(choice):
        line = input("Write any line : ")
        file.write(line)
        file.write('\n')
    file.close()

#Results function
def get_results():
    letter = " "
    file = open("letter_file.txt", "r")
    vowel_count = 0
    consonant_count = 0
    upper_count = 0
    lower_count = 0
    while letter:
        letter = file.read(1)
        if letter in vowels:
            vowel_count += 1
        else:
            None
        if letter in consonants:
            consonant_count += 1
        else:
            None
        if letter.islower() == True:
            lower_count += 1
        else:
            None
        if letter.isupper() == True:
            upper_count += 1
        else:
            None
    print("Number of vowel characters in the file are",vowel_count)
    print("Number of Lowercase characters in the file are",lower_count)
    print("Number of Uppercase characters in the file are",upper_count) 
    print("Number of consonant characters in the file are",consonant_count)
    file.close()

#Calling the function
write_file()
get_results()
