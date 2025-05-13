def longest_consecutive(array):
    """
    Returns the length of the maximum consecutive numbers in the array. 
    """
    if not array:  # Handle the case where the array is empty
        return 0

    array = sorted(array)
    max_length = 1  # The minimum length of a consecutive sequence is 1
    length = 1

    for i in range(1, len(array)):
        if array[i] - array[i - 1] == 1:
            length += 1

        elif array[i] != array[i - 1]:  # Handle duplicates
            max_length = max(max_length, length)  # Update max_length
            length = 1  # Reset length for a new sequence

    # Check the last sequence
    return max(max_length, length)


test_cases = [
    ([100, 4, 200, 1, 3, 2], 4),   # Sequence: [1, 2, 3, 4]
    ([0,3,7,2,5,8,4,6,0,1], 9),    # Sequence: [0,1,2,3,4,5,6,7,8]
    ([9, 1, 4, 7, 3, -2, 2, 0, -1, 5, 8, -3, 6], 13), # [-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
    ([1, 2, 3, 4, 5], 5),  # Already sorted, max sequence is full array
    ([10, 30, 20, 40], 1), # No consecutive sequences, max length is 1
    ([5, 5, 5, 5], 1),  # Duplicates, only one number counts
    ([], 0)  # Empty array, no sequence
]

for test, output in test_cases:
    print(f"Test {test}: {longest_consecutive(test)} == {output}")