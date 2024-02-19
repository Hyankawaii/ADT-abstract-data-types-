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
            print("while pass", array)

        array[place + 1] = buffer
        print(array)

print(array)

DECLARE data : ARRAY[0:6] OF INTEGER
DECLARE Upper, lower, buffer, temp, place, index:INTEGER

upper <-- LENGTH(data)
lower <-- 0
FOR index  <-- 1 TO LENGTH (array) 
    place <-- index - 1
    BUFFER <-- array(index)
    IF buffer > array[place] THEN
        WHILE array[place + 1] > array[place] AND place >= 0
            temp <-- array[place]
            array[place] <-- array[place + 1]
            array[place + 1] <-- temp
            place = place + 1
        ENDWHILE
    ENDIF
ENDFOR

            