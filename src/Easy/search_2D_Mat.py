"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
import sys

class Solution:

    def Binary_Search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # This is basically a binary search but for a 2D vectorial space.
        # The idea is pretty much the same, only we will eliminate rows rather than number intervals.

        l, r = 0, len(matrix[0]) - 1 # Left to right for columns
        t, b = 0, len(matrix) - 1 # Top to bottom for rows

        while t <= b: 
            mid_row = (t + b) // 2

            if matrix[mid_row][l] < target and matrix[mid_row][r] < target: # All rows above are useless.
                t = mid_row + 1

            elif matrix[mid_row][l] > target and matrix[mid_row][r] > target: # All rows bellow are useless.
                b = mid_row - 1 
            
            else:
                return self.Binary_Search(matrix[mid_row], target)
            
        return False

if __name__ == "__main__":

    if len(sys.argv) < 1:
        print("Usage: python3 search_2D_Mat.py <target>")
        sys.exit(1)

    sol = Solution()

    mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    
    target = int(sys.argv[1])
    print(f"Target: {target} is {"not" if not sol.searchMatrix(mat, target)else ""} in the matrix.")

