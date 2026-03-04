"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""
import sys 

class Solution:
    def choppedSqrt(self, x: int) -> int:
        # A binary search can be used to find an i number so that i*i is the closest to our target number: x
        if x < 1:
            return x
        nums = range(x)
        l, r = 0, x - 1

        while l <= r:
            mid = (r+l) // 2
            i = nums[mid]

            if i*i == x:
                return nums[mid]
            elif i*i < x:
                l = mid + 1
            else: 
                r = mid - 1

        return l - 1 # We want to round downwards. 
    
if __name__ == "__main__":

    if len(sys.argv) < 1:
        print("Usage: python3 sqrt_x.py <x>")
        sys.exit(1)

    sol = Solution()
    
    x = int(sys.argv[1])
    print(f"For {x} the aproximate root is: {sol.choppedSqrt(x)}")
