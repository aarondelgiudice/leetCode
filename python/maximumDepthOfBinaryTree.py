"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # any solution: solve for the base case first
        depth = 0
        
        # node is empty, return nodeCount
        if not root:
            return depth

        # solution 1: recursive depth first search
        # time: O(n) b/c we have to search the entire tree
        # mem: O(n) for worst case b/c we have to search the max height of tree
        
        # recursively search left, right leaf nodes
        # return the max nodeCount of either direction of the leaf nodes
        depth += 1 # +1 for current node
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right))

        return depth

        # solution 2: iterative depth first search
        # time: O(n) we have to scan the entire tree
        # mem: O(n) we have to scan the entire tree
        
        # initialize a stack
        # stack contains current node and level
        curr = 1 # current level
        stack = [(root, depth + 1)]

        while stack:
            node, curr = stack.pop()
        
            if node:
                depth = max(curr, depth)
                stack.append((node.left, curr+1))
                stack.append((node.right, curr+1))

        return depth

        # solution 3: iterative breadth first search
        # time: O(n) we have to scan the entire tree
        # mem: O(n) we have to scan the entire tree
        
        # # initialize queue with single value
        q = deque([root])

        # iterate over queue until it is empty:
        while q:
            # loop over queue and remove all elements
            for _ in range(len(q)):
                # pop first element from queue
                node = q.popleft()
                
                # if node.left has any elements, add them to the queue
                if node.left is not None:
                    q.append(node.left)
                
                # if node.right has any elements, add them to the queue
                if node.right is not None:
                    q.append(node.right)

            # increment depth for current node
            depth += 1

        return depth


if __name__ == "__main__":
    INPUTS = (
        # root: List[int]               expected: int
        ((3, 9, 20, None, None, 15, 7), 3),
        ((1, None, 2),                  2),
    )

    for root, expected in INPUTS:
        actual = Solution().maxDepth(root)
        # assert actual == expected, f"{actual=}, {expected=}, {root=}"
