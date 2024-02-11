array = [7,20,6,54,8,100,12]

upper = len(array)
lower = 0
index = lower + 1
for index in range(upper):
    buffer = array[index]
    place = index - 1
    if buffer < array[place]:
        while place >= lower and buffer < array[place]:
            temp = array[place + 1]
            array[place + 1] = array[place]
            array[place] = temp
            place = place - 1

        array[place + 1] = buffer

print(array)
        