#Writing in the file
def write_file():
    file = open("vowel_words.txt", "w")
    choice = int(input("How many lines you want to enter : "))
    for i in range(choice):
        lines = input("Enter any line : ")
        file.write(lines)
        file.write("\n")

#Checking vowel words
def vowel_counts():
    vowel_count = 0
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    file = open("vowel_words.txt", "r")
    data = file.read()
    data = data.split()
    for i in data:
        if i[0] in vowels:
            vowel_count += 1
    print("Number of words starting with vowels in the file are", vowel_count)

write_file()
vowel_counts()
