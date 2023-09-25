"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a
value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

source: https://leetcode.com/problems/range-sum-of-bst/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # recursion
        if not root:
            return 0

        sum = 0

        if root.val < low:
            # exclude left branch
            # all nodes in left branch will be less than root.val
            # so we can skip them as they will not be in range(low, high)
            sum += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            # exclude right branch
            # all nodes in right branch will be greater than root.val
            # so we can skip them as they will not be in range(low, high)
            sum += self.rangeSumBST(root.left, low, high)
        else:
            sum += root.val
            sum += self.rangeSumBST(root.left, low, high)
            sum += self.rangeSumBST(root.right, low, high)
        
        return sum

        # depth first search
        sum = 0

        def dfs(root):
            nonlocal sum
            
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            
            if root.left and low <= root.left.val <= high:
                sum += root.left.val
            
            if root.right and low <= root.right.val <= high:
                sum += root.right.val
            
            return sum
        
        if low <= root.val <= high:
            sum += root.val

        return dfs(root)
