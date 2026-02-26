"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

NOTE: This a book example an application of a binary search algorithm. 
"""
import sys 

class Solution(object):


    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums)-1
        while l <= r: 
            mid = (r+l) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l # We don't really care if the array has our target, for we have the instruction to return the index it would take. 
        
    
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 Search_Insert_Pos.py <target> <num1> <num2> ...")
        sys.exit(1)

    sol = Solution()
    
    target = int(sys.argv[1])
    nums = [int(x) for x in sys.argv[2:]]

    print(f"For array: {nums}\nAnd target: {target}\nOutput is: {sol.searchInsert(nums, target)}")

