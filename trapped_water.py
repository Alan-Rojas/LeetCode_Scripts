def trapped_water(array):
    """
    Recieves an array of heights of an historgram. (list)
    For some reason, it rained on the histogram. This function returns the units of water trpped. (int)
    """
    """ 
    Ok, so what I wanna do the following:
    identify the lowest point in the array, and if both neighbors (right and left) are both higher, add one unit to the trapped water.
    If one of the neigbours is of the same height
    Also, I must add one unit to that point because it's now filled with water. 
    Then, again, look for the next lowest point
    
    """
    water_trapped = 0


    for _ in array:

        lowest = array.index(min(array))
        if (lowest == 0): #If the lowest is the first, no water can be trapped, thus, let's make it equal to its neighbor
            if array[lowest] == array[lowest+1]: # If they are both equal sum 1 to both (no water can be trapped).
                array[lowest] += 1
                array[lowest+1] +=1
            else:
                array[lowest] = array[lowest+1]

        elif (lowest == len(array)-1): #If the lowest is the last, no water can be trapped, thus, let's make it equal to its neighbor
            if array[lowest] == array[lowest-1]:    
                array[lowest] += 1
                array[lowest-1] +=1
            else:
                array[lowest] = array[lowest-1]

        else: 
            if (array[lowest+1] > array[lowest]) and (array[lowest-1] > array[lowest]):
                water_trapped += 1
                array[lowest] += 1 # Because it is now filled with water. 

    return water_trapped

test_cases = [[0,1,0,1], [0,0,0], [2,2,1,1], [5,2,3,4]]

for test in test_cases:
    print(f"Test: {test}__ Water Trapped: {trapped_water(test)}")
