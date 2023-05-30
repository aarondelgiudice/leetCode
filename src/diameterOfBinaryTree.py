"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

source: https://leetcode.com/problems/diameter-of-binary-tree/ 
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = height of right sub tree + height of left subtree
        # height = current position (1) + max(right subtree depth, left subtree depth)
        
        # initialize a global diameter value
        diameter = 0
        
        # define depth frist search recursive function
        def dfs(root):
            nonlocal diameter # allow dfs() to edit diameter var

            if not root:
                # height of a null tree is -1 (not 0)
                # the height of a single node is 0 (not 1)
                return -1

            # recursively find height of left, right subtress
            left = dfs(root.left)
            right = dfs(root.right)

            # find current diameter = left height + right height
            curr = (1 + left) + (1 + right)
            # if curr > global diameter, update global diameter var
            diameter = max(curr, diameter)

            return 1 + max(left, right)

        # call recursive function to process tree and update global diameter variable
        dfs(root)

        return diameter


if __name__ == "__main__":
    INPUTS = (
        # root: List[int]   expected: int
        ((1, 2, 3, 4, 5),   3),
        ((1, 2),            1),
    )

    for root, expected in INPUTS:
        actual = Solution().diameterOfBinaryTree(root)
        # assert actual == expected, f"{actual=}, {expected=}, {root=}"
