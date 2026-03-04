def romanToInt(s: str):
    """
    This function takes an ACTUAL roman number: str(s)
    """
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    nums = [numbers[vals] for vals in s]

    for n in range(len(nums)-1): 
        if nums[n] < nums[n+1]:
            nums[n] *= -1

    return sum(nums)

print(romanToInt("XXIX"))

