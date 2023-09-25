"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

source: https://leetcode.com/problems/subtree-of-another-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # see leetCode 100. Same Tree for ref
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            left, right = self.sameTree(p.left, q.left), self.sameTree(p.right, q.right)

            return (left == True) and (right == True)

        def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # handle base case(s)
            # if subRoot is null it will always be a subtree of root
            if not subRoot:
                return True

            # if subRoot is not null but root is null,
            # subRoot cannot be a subtree of root
            if not root and subRoot:
                return False

            # first check if root and subRoot are the same tree
            if self.sameTree(root, subRoot):
                return True

            # next recursively check if subRoot is subtree of root.left/right
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            
            return (left == True) or (right == True)

if __name__ == "__main__":
    INPUTS = (
        # root: List[int]                   subRoot: List[int]  expected: bool
        ((3,4,5,1,2),                       (4,1,2),            True),
        ((3,4,5,1,2,None,None,None,None,0), (4,1,2),            False),
    )

    for root, subRoot, expected in INPUTS:
        actual = Solution().isSubtree(root, subRoot)
        # assert actual == expected, f"{actual=}, {expected=}, {root=}, {subRoot=}"