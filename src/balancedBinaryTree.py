"""
Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

source: https://leetcode.com/problems/balanced-binary-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # function returns a tuple: (balanced: bool, height: int)
            # first handle base case: root node is null
            if not root:
                # an empty node is technically balanced
                # but has a height of 0
                return (True, 0)

            # recursively call function and left and right nodes
            leftBal, leftHeight = dfs(root.left)
            rightBal, rightHeight = dfs(root.right)

            # +1 for current node + max height of left/right leaf nodes
            height = 1 + max(leftHeight, rightHeight)

            # either left/right leaf node is unbalanced, then return False
            if not (leftBal and rightBal):
                return (False, height)

            # if height difference between left/rigth leaf nodes is greater than 2,
            # then return false
            if not abs(leftHeight-rightHeight) < 2:
                return (False, height)

            # else: balanced is true and height difference is < 2
            return (True, height)

        return dfs(root)[0] # only return boolean


if __name__ == "__main__":
    INPUTS = (
        # root: List[int]               expected: bool
        ((3,9,20,None,None,15,7),       True),
        ((1,2,2,3,3,None,None,4,4),     False),
        ((),                            True),
    )

    for root, expected in INPUTS:
        actual = Solution().isBalanced(root)
        # assert actual == expected, f"{actual=}, {expected=}, {root=}"
