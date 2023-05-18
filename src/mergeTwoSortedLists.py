"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

source: https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next

            else: # list1.val >= list2.val
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        if list1: # return list1 if not None
            temp.next = list1
        elif list2: # return list2 if not None
            temp.next = list2
        
        return dummy.next


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # List[int], List[int], output: List[int]
        ([1,2,4], [1,3,4],      [1,1,2,3,4,4]),
        ([], [],                []),
        ([], [0],               [0])
    )

    mySolution = Solution()

    for list1, list2, expected in INPUTS:
        print(f"list1: {list1}, list2: {list2}, output: {expected}")
        actual = mySolution.mergeTwoLists(list1, list2)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
