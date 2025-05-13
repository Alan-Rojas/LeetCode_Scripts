def merge_intervals(array):
    """
    Takes an array if intervals (integer intervals) and returns the overlapping intervals.
    """
    """
    Ok, let's think this trough. The intervals are not sorted, that's a problem. (I am asuming intervals are closed, meaning inclusive)
    ex. [0, 1][1, 2] = [0, 2]
    Also note two intervals are overlapping if the difference between the last element of one and the first element of the other greater or equal to 0.
    AS LONG AS THEY ARE SORTED!
    ex. [0, 1][1, 2] = 0; [-4, 0][-1, 2]  = 1; [-4, -1][-2, -1] = 1, [1, 4][2, 3] = 2. 
    ex. [0, 1][2, 5] = -1; [-4, -1][0, 2] = -1; [-4, -2][-1, 4] = -1

    This means I have to sort the array first. 
    To sort the arrays imma do the following, create a dictionary, iterate trough the first element of each interval, and save it in a dictionary along with the index.
    """
  
    array.sort(key=lambda x: x[0]) #I am sorting the intervals by their first element
    
    if len(array) > 0:
        sol = [array[0]] # The first interval will be the first array
    else: 
        sol = []

    #
    for i in range(1, len(array)):  
        last = sol[-1]  # Last interval in solution
        current = array[i]  # Current interval

        if last[1] >= current[0]:  # Overlapping
            sol[-1] = [last[0], max(last[1], current[1])]  # Merge
        else:
            sol.append(current)  # No overlapping, then just add the interval.

    return sol


test_cases = [

    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),  
    ([[1, 4], [4, 5]], [[1, 5]]),  

    ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], [[1, 10]]),  # Nested intervals  
    ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),  # No merging needed  
    ([[1, 5]], [[1, 5]]),  # Single interval  
    ([], []),  # Empty list  

    # Unsorted input
    ([[8, 10], [1, 3], [15, 18], [2, 6]], [[1, 6], [8, 10], [15, 18]]),  

    # Negative numbers
    ([[-5, -1], [-10, -6], [-4, 0]], [[-10, -6], [-5, 0]]),  
    ([[-3, -2], [-1, 1], [2, 3]], [[-3, -2], [-1, 1], [2, 3]]),  # No merging  

    # Large overlapping
    ([[1, 100], [50, 200], [150, 300]], [[1, 300]]),  
]

for i, (test, expected) in enumerate(test_cases):
    result = merge_intervals(test)
    assert result == expected, f"Test {i+1} failed: expected {expected}, got {result}"
print("All tests passed!")       

        
        


