def removeDuplicates(array):
    """
    Ok so my idea is to create a variable to track if repetition is allowed. 
    There are two possible states, right, either the last element is equal to the next, or it is not. 
    """
    equal_count = 0
    for i in range(1, len(array)):

        if array[i-1] == array[i]:
            equal_count +=1
        else: 
            equal_count = 0

        if equal_count > 1:
            if (i+1 == len(array)): #If its the last element, just switch it
                array[i] = "_"
            else:
                array[i:len(array)-1] = array[i+1:]
                array[-1] = "_"

    return array

print(removeDuplicates([0,0,1,1,1,1,2,3,3]))