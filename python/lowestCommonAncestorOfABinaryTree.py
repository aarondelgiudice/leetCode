"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
The number of nodes in the tree is in the range [2, 10**5].
-10**9 <= Node.val <= 10**9
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

def main():
    TEST_CASES = (
        # root                          p   q   expected
        ([6,2,8,0,4,7,9,None,None,3,5], 2,  8,  6),
        ([6,2,8,0,4,7,9,None,None,3,5], 2,  4,  2),
        ([2,1],                         2,  1,  2),
    )

    for root, p, q, expected in TEST_CASES:
        actual = Solution().lowestCommonAncestor(make_tree(root), TreeNode(p), TreeNode(q))
        assert actual.val == expected, (actual.val, expected)

    return

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    nodes = [root]
    for i in range(1, len(values)):
        if values[i] is not None:
            node = TreeNode(values[i])
            nodes.append(node)
            if i % 2 == 1:
                nodes[0].left = node
            else:
                nodes[0].right = node
        if i % 2 == 0:
            nodes.pop(0)

    return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # NOTE: Since we are guaranteed that p and q exist in the tree, we do not need to check for edges cases.
        while root:
            # if the value of p and q is greater than root, then LCA will be in the right subtree
            if root.val < min(p.val, q.val):
                root = root.right

            # if the value of p and q is less than root, then LCA will be in the left subtree
            elif root.val > max(p.val, q.val):
                root = root.left

            # if one value is less and the other is greater, then root is the LCA
            else:
                return root

if __name__ == "__main__":
    main()
    