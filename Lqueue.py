Max_Size = 6
Array =[None for i in range(Max_Size)]
front = 0
rear = -1
def Is_Empty():
    if front > rear:
        return True
    else:
        return False
def Is_Full():
    if rear == (Max_Size - 1):
        return True
    else:
        return False
def enqueue(value):
    if Is_Full() == True:
        print("queue is already full, value could not be added")
    else:
        global rear
        rear += 1
        Array[rear] = value
def dequeue():
    global rear
    if Is_Empty()== True:
        print("queue is empty, no items to dequeue")
    else:
        Array[rear] = None
        rear -= 1

enqueue(5)
enqueue(10)
enqueue(10)
enqueue(10)
enqueue(10)
enqueue(10)
print(Array)
dequeue()
print(Array)
enqueue(10)
enqueue(10)
print(Array)
