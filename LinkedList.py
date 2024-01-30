max_size = 5
List = [None for i in range(max_size)]
LLPointer = [0 for i in range(max_size)]
for i in range(max_size):
    if i == (max_size - 1):
        LLPointer[i] = -1
    else:
        LLPointer[i] = i+1
print(LLPointer)
Sp = -1
Hp = 0  

def Is_Empty():
    global Sp
    empty = False
    if Sp == -1 :
        empty = True
    return empty

def Is_Full():
   global Hp
   if Hp == -1:
       return True
   else:
       return False
   
def insert(value):
    global Sp
    global Hp
    if Is_Full() == False:
        TempSp = Sp
        Sp = Hp
        List[Sp] = value
        Hp = LLPointer[Hp]
        LLPointer[Sp] = TempSp    #start pointer always points to the start of the list#
    else:
        print("linked list is full ")

def search(value):
    global found
    found = False
    for i in range(len(List)):
        if List[i] == value:
            found = True
            index = i
    if found == True:
        print("value inputted is found")
        search_index = index
    else: 
        search_index = -1
    return search_index

def search2(value):
    index = Sp
    while List[index] != value and LLPointer[index] != -1:
        index = LLPointer[index]
    if index == -1:
        print('the value does not exist')
    else:
        return index

def delete(value):
    global Hp
    oldindex = -1
    index = Sp
    while List[index] != value and LLPointer[index] != -1:
        oldindex = index
        index = LLPointer[index]
    if index == -1:
        print('the value does not exist')
    else:
        if oldindex != -1:
            List[index] = None
            LLPointer[oldindex] = LLPointer[index]
            LLPointer[index] = Hp
            Hp = index
        else:
            List[index] = None
            LLPointer[index] = -1
            Hp = index
 

insert(5)
print(List)
print(LLPointer)
insert(5)
print(List)
print(LLPointer)
insert(57)
print(List)
print(LLPointer)
insert(5)
print(List)
print(LLPointer)
insert(55)
print(List)
print(LLPointer)
insert(55)
print(List)
print(LLPointer)
insert(5)
print(List)
print(LLPointer)
delete(57)
print(List)
print(LLPointer)