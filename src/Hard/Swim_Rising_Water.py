"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time. 
At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. 
You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
"""
# Ok so this is basically a maze, trying to find the shortest path to the end. 
# In this case, the maze begins at the top left corner, ends at the bottom right, and we define shortest as the least time-spending solution.

# The way I understand it is as if we were pouring water, when a position (anywhere on the map) is lower than the current level, water goes there.
# Thus, we need a way to keep every option stored... Maybe a Heap...
# So... Look at a solution, add it's choices to the heap. -> Pop the smallest, and ad its choices to the heap. 
# -> Repeat until we reach the sol.
#  
import heapq
import sys

class MySolution:

    def path_options(self, i, j, n):

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        options = [(a,b) for a, b in directions if 0 <= i+a < n and 0 <= j+b < n]

        return options
    
    def choices(self, i, j, matrix, drowned, choices_heap):
        op = self.path_options(i, j, len(matrix))

        for o in op:
            if (i + o[0], j + o[1]) not in drowned:
                data = (matrix[i + o[0]][j + o[1]], i + o[0] , j + o[1])
                heapq.heappush(choices_heap, data)
    
        return choices_heap    

    def sol_reached(self, i, j, n):
        return i == j == n-1 # When our smallest is this, we have reached it. 

    def swimInWater(self, grid: list[list[int]]) -> int:
        i, j = 0, 0 # This is my starting position
        n = len(grid)
        choices_heap = [] # This will simulate the water flow,
        drowned = set() # Avoiding choosing squares that are already filled with water.
        max_water = grid[0][0]

        # Loop
        while not self.sol_reached(i, j, n):
            drowned.add((i, j))
            choices_heap = self.choices(i, j, grid, drowned, choices_heap)

            _, i, j = heapq.heappop(choices_heap)

            if grid[i][j] > max_water:
                max_water = grid[i][j]
        
            
        return max_water
    
