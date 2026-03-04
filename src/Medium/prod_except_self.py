import math 

def array_prod_except_self(array):
    """
    Takes an array of integers (nums) and outputs an array (answers) of the same size.
    Note: answers[i] is equal to the product of all the elements except nums[i]. 
    Division cannot be used.
    """
    # So, I am thinking maybe trying to avoid multiplying by this number, right? 
    # What if i just take the index, and do left prod, and right prod?
    new_array = []
    
    for i in range(len(array)):
        left_prod = math.prod(array[:i])
        right_prod = math.prod(array[i+1:])
        new_array.append(left_prod*right_prod)
    
    return new_array

ex_arrays = [[1,2,3,4],[0, 1, 2, 3], [-1, 2, -3, 4],[1000, 2000, 3000, 4000],[1],[0,0,0,0],[2,2,2,2]]

# Run test cases: 
for test in ex_arrays:
    print(f"Test Result: {array_prod_except_self(test)}")
