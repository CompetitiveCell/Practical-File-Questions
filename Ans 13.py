def LShift(arr, n):
    length = len(arr)
    for x in range(0,n):
        y = arr[0]
        for i in range(0,length-1):
            arr[i] = arr[i+1]
        arr[length-1] = y
    print(arr)

arr = eval(input("Enter a list : "))
n = int(input("Enter how many elements to shift : "))
LShift(arr, n)
