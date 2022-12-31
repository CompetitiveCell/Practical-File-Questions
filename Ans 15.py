def index_list(number_list):
    index_lst = []
    for i in range(len(number_list)):
        if number_list[i] != 0:
            index_lst.append(i)
    print(index_lst)

number_list = eval(input("Enter a list of numbers including 0 and other numbers : "))
index_list(number_list)
