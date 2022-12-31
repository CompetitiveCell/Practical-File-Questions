def isempty(stk):
    if stk == []:
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk)-1

def pop(stk):
    if isempty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk)-1
        return item

def peek(stk):
    if isempty(stk):
        return "Underflow"
    else:
        top = len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        print("Stack Empty")
    else:
        top = len(stk)-1
        print(stk[top],"is the top")
        for i in range(top-1, -1, -1):
            print(stk[i])

stack = []
top = None

while True:
    print("STACK OPERATIONS")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")
    ch = int(input("Enter you choice(1-5) : "))
    if ch == 1:
        item = int(input("Enter item : "))
        push(stack, item)
    elif ch == 2:
        item = pop(stack)
        if item == "Underflow":
            print("Stack is empty")
        else:
            print("Popped item is", item)
    elif ch == 3:
        item = peek(stack)
        if item == "Underflow":
            print("Stack is empty")
        else:
            print("Topmost item is", item)
    elif ch == 4:
        display(stack)
    elif ch == 5:
        break
    else:
        print("INVALID CHOICE")
