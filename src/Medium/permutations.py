"""
Given an array nums of distinct integers, return all the possible . 
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Classic permutation problem, easy solvable with backtracking.
        # The idea is to explore the decision tree of possible combinations. 
        # 

        res = []

        def backtracking(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in nums:
                if n not in perm:
                    perm.append(n)
                    backtracking(perm)
                    perm.pop()


        backtracking([])
        return res


        
            


