"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

source: https://leetcode.com/problems/minimum-path-sum/
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # complexity: O(m*n)
        
        # handle edge cases
        if not grid or len(grid) == 0:
            return 0

        # solve
        m, n = len(grid), len(grid[0])

        # sum values along x-axis of row1 
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        # sum values along y-axis of col1
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        # traverse m,n matrix and sum min value of each option of each step
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # value of last step is sum of minimum path    
        return grid[-1][-1]

if __name__ == "__main__":
    INPUTS = (
        # grid: List[List[int]],    output: int
        ([[1,3,1],[1,5,1],[4,2,1]], 7),
        ([[1,2,3],[4,5,6]],         12),
    )

    mySolution = Solution()

    for grid, expected in INPUTS:
        print(f"grid: {grid}, output: {actual}")
        actual = mySolution.minPathSum(grid)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
