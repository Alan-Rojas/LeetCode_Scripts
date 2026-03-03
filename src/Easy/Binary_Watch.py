"""
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). 
Each LED represents a zero or one, with the least significant bit on the right.

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. 

You may return the answer in any order.

The hour must not contain a leading zero.

    For example, "01:00" is not valid. It should be "1:00".

The minute must consist of two digits and may contain a leading zero.

    For example, "10:2" is not valid. It should be "10:02".

"""
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:

        sol = []

        def num_bits(n):
            bits = 0

            while n >= 1:
                bits += n % 2
                n = n//2

            return bits
                
        def to_string(h, m):
            if m < 10:
                return f"{h}:0{m}"
            else:
                return f"{h}:{m}"
            
        for h in range(12):
            for m in range(60):
                if num_bits(h) + num_bits(m) == turnedOn:
                    sol.append(to_string(h,m))
        
        return sol

        

            



