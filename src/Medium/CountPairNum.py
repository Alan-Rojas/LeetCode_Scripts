"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper

 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

"""

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:

        nums.sort()

        def count_less_than(limit):
            count = 0
            l, r = 0, len(nums) - 1

            while l < r:

                if nums[l] + nums[r] > limit:
                    r -= 1

                else:
                    count += r -l

                    l += 1
            return count
        
        return count_less_than(upper) - count_less_than(lower - 1)


                

