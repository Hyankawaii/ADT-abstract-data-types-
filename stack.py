    max_size = 10
Stack = [None for i in range(max_size)]

top = -1 #required for some reason
#DECLARE item : Integer
 
def Is_Empty():
    global top
    Empty_flag = bool(0)
    if top == -1:
        Empty_flag = bool(1)
    return Empty_flag
 
def Is_Full():
    global top
    full_flag = bool(0)
    if top == max_size - 1:
        Empty_flag = bool(1)
    return full_flag

def push(value):
    global top
    if Is_Full() == True:
        print("stack is full cannot push, stack overflow")
    else:
        top += 1
        Stack[top] = value

def pop():
    global top
    var = Is_Empty()
    if Is_Empty() == True:
        print("stack is empty cannot pop, stack underflow")
    else:
        item = Stack[top]
        Stack[top] = None
        top -= 1
        return item
def peek():
    global top
    var = Is_Empty()
    if Is_Empty() == True:
        print("stack is empty cannot pop, stack underflow")
    else:
        item = Stack[top]
        return item
push(10)
print(Stack)
pop()
print(Stack)