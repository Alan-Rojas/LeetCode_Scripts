def intToRoman(num):
    """
    Right, so I am gonna need a dictionary for the values in roman numerology.
    After that, I am goint to need to try this: divide the number by the values of roman from highest to lowest, 
    then substract the amount to the actual number. 
    """
    vals = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
        "XC": 90, "L": 50, "XL": 40, "X": 10,
            "IX": 9, "V": 5,"IV": 4, "I":1
        }

    roman = ""

    for char, val in vals.items():

        res = num//val

        if res > 0:
            roman += char*res
            num -= res*val


    return roman