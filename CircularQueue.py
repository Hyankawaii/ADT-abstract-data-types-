Max_Length = 5
CQ = [None for i in range(Max_Length ) ]
Queue_length = 0
Front_pointer = 0
rear_pointer = -1

def queue(item):
    global rear_pointer
    global Queue_length
    if Queue_length < Max_Length:
        if rear_pointer < (len(CQ) - 1):
            rear_pointer = rear_pointer + 1
        else:
            rear_pointer = 0
        CQ[rear_pointer] = item
        Queue_length += 1
    else:
        print("queue is full, item", item, "could not be queued")

def dequeue():
    global Front_pointer
    global Queue_length
    if Queue_length <= 0 :
        print("the queue is empty, cannot dequeue")
    else:
        item = CQ[Front_pointer]
        if Front_pointer < (len(CQ) - 1):
            Front_pointer = Front_pointer + 1
        else:
            Front_pointer = 0
        Queue_length -= 1
        print(item)
queue(100)
queue(12)
queue(4)
queue(34)
queue(282)
queue(24)
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
queue(25)
dequeue()
