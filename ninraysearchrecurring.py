data_set = [0,1,2,3,4,5,6,7,8,9]
print (data_set)
def recursearch(item, high, low ):
    mid = (high + low)//2
    found = False
    if mid == item :
        found = True 
        return mid 
    elif item > mid and low != (high - 1):
        low = mid + 1
        recursearch(item, high, low )
    elif item < mid and high != 1:
        high = mid -1
        recursearch(item, high, low )
    else:
        pain = -1
        if found == False:
            return pain
    
print(recursearch(10, len(data_set), 0 ))    
    
