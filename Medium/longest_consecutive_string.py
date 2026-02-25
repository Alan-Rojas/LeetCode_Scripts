def longest_substring(string):
    """
    Takes a string and returns the lenght of the largest consecutive substring that does not repeat characters.
    """
    longest = []
    lenghts = []

    for i in string:

        if i not in longest: 
            longest.append(i)
            
        else: 
            lenghts.append(len(longest))
            longest = [i]
            
    lenghts.append(len(longest))

    
    return max(lenghts)


test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("abcdef", 6),
    ("", 0),
    ("a", 1),
    ("dvdf", 3),
    ("pwwkew", 3),
]
for test, res in test_cases:
    print(f"Test: {test}\n res: {longest_substring(test)} == {res}")