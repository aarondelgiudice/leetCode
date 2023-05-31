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
        def dfs(root: Optional[TreeNode]):
            # function returns a tuple: (isBalanced: bool, subtreeHeight: int)
            # first handle base case: root node is null
            if not root:
                # an empty node is technically balanced
                # but has a height of 0
                return (True, 0)
            
            # recursively call function and left and right nodes
            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)

            # check if subtree is balanced:
            # (|leftHeight - rightHeight| < 2) and (left, right subtrees are balanced)
            heightDiff = abs(leftHeight-rightHeight)

            isBalanced = (heightDiff < 2 and leftBalanced and rightBalanced)

            # get height of subtree: nodeHeight + max height left/right nodes
            nodeHeight = 1 # if node is not null, it has a height of 1
            subtreeHeight = nodeHeight + max(leftHeight, rightHeight)
            
            return (isBalanced, subtreeHeight)

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
