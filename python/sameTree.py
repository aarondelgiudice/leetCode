"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 
Constraints:
The number of nodes in both trees is in the range [0, 100].
-10**4 <= Node.val <= 10**4

source: https://leetcode.com/problems/same-tree/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # handle base case(s)
        if not p and not q:
            return True # nodes are null, but match
        if not p or not q:
            return False # nodes are null, but do not match
        if p.val != q.val:
            return False # nodes are not null, but do not match

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return (left == True) and (right == True) # left/right cases have to match


if __name__ == "__main__":
    INPUTS = (
        # p: List[int]  q: List[int]    expected: bool
        ((1, 2, 3),     (1, 2, 3),      True),
        ((1, 2),        (1, None, 2),   False),
        ((1, 2, 1),     (1, 1, 2),      False),
    )

    for p, q, expected in INPUTS:
        actual = Solution().isSameTree(p, q)
        # assert actual == expected, f"{actual=}, {expected=}, {p=}, {q=}"
