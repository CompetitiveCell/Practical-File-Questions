def create(year_tuple):
    year_list = list(year_tuple)
    length = len(year_list)
    print(length)
    months_list = []
    days_list = []
    for i in range(length):
        if i%2 == 0:
            months_list.append(year_list[i])
        elif i%2 != 0:
            days_list.append(year_list[i])
        else:
            None
    months_tuple = tuple(months_list)
    days_tuple = tuple(days_list)
    print("Months tuple is", months_tuple)
    print("Days tuple is", days_tuple)

choice = int(input("Enter how many months to enter : "))
year_list = []
for i in range(choice):
    months = input("Enter month's name : ")
    days = int(input("Enter it's number of days : "))
    year_list += months, days

year_tuple = tuple(year_list)

create(year_tuple)
