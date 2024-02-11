array = [1,3,7,4,7665,87,54,78]
swap = True
while swap == True:
    i = 0
    swap = False
    for i in range(len(array)- 1):
        if array[i] > array[i+1] :
            swap = True
            buffer = array[i]
            array[i] = array[i + 1]
            array[i + 1] = buffer
print(array)

def search(value):
    global array
    upper = len(array)
    lower = 0
    mid = (upper - lower) // 2
    print(array[int(mid)])
    found = False
    while found != True and mid !=lower and mid != upper:

        if value == array[mid]:
            found = True
        elif value > array[mid]:
            lower = mid + 1
            mid = (upper - lower) // 2
        else:
            upper = mid - 1
            mid = (upper - lower) // 2
    if found == True:
        print("value found")
    else:
        print("value not found")
search(8)