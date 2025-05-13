def longestCommonPrefix(strs):
    """
    Iterate trough the first string's letters. If the letter is the first as
    """

    
    common_string = ""
    smallest = min(strs)

    for i in range(len(smallest)):
        letter = smallest[i]
        if all(letter == word[i] for word in strs): # smallest[i] is in all words:
            common_string += letter 

        else:
            return common_string