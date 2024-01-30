MAX_SIZE = 6
LinearQ = [None for i in range(MAX_SIZE)]
FrontPointer = -1
BackPointer = -1
def IsEmpty():
    if FrontPointer == -1:
        return True
    else:
        return False
    
def IsFull():
     if ((BackPointer + 1) % MAX_SIZE == FrontPointer): 
        return True
     else:
         return False
    
def Enqueue(Item):
    global BackPointer
    global FrontPointer
    if IsFull() == True:
        print("Queue is full, cannot add any more items")
    else:
        if FrontPointer == -1:
            FrontPointer = 0
            BackPointer = 0
            LinearQ[BackPointer] = Item
        else:
            BackPointer = (BackPointer + 1) % MAX_SIZE
            LinearQ[BackPointer] = Item

def Dequeue():
    global FrontPointer
    global BackPointer
    if IsEmpty() == True:
        print("Queue is empty, unable to dequeue")
    else:
        if FrontPointer == BackPointer:
             Item = LinearQ[FrontPointer]
             LinearQ[FrontPointer] = None
             FrontPointer = -1
             BackPointer = -1
             return Item
        else:
            Item = LinearQ[FrontPointer]
            LinearQ[FrontPointer] = None
            FrontPointer = (FrontPointer + 1) % MAX_SIZE
            return Item
    
print(IsEmpty())
print(IsFull())
Enqueue(123)
Enqueue(100)
Enqueue(11)
Enqueue(12)
Enqueue(13)
Enqueue(7)
Enqueue(1)
print(LinearQ)

for i in range(7):
    print(Dequeue())
    print(LinearQ, FrontPointer, BackPointer)

for i in range(7):
    Enqueue(2)
    print(LinearQ)
