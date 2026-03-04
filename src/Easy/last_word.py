def lengthOfLastWord(s):
    """
    Since I am only focused on the lenght of a word, we'll just focus on either getting to the end of the string or finding a blank space.
    What if the last character is a whitespace? Just ignore it, then.
    """
    l = 0
    str_l = len(s)
    first_letter = False


    for i in range(1, str_l+1):
        if s[-i] != " ":
            first_letter = True
            l += 1
    

        if ((s[-i] == " ") and first_letter) or (i == str_l):
            return l
    return l 