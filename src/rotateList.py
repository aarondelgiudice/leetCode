"""
Rotate List
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

source: https://leetcode.com/problems/rotate-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # handle edge cases: we can't perform rotations if linked list is empty
        # so return linked list
        if not head:
            return head
        
        # get length and tail of linked list
        # length == 1 b/c we know that we have at least 1 input node that is not null
        # set the tail node to the head node b/c we know that at leas the head node is not null
        length, tail = 1, head
        
        # while there is a next node to iterate to; e.g. node.next is not null
        # set tail to next node and increment length by 1
        while tail.next:
            tail = tail.next
            
            length += 1
        
        # mod k by input length to reduce it to a number that is less than the length
        # e.g. if k = 25 and length = 5, set k to value <= 5
        k = k % length

        # if modded k == 0 then there is no rotation as k is a multiple of lenth of list
        # e.g. if k = 5 and length = 5 then rotated list will match input list
        if k == 0:
            return head
        
        # move to pivot and perform rotate
        # set current node to head node
        cur = head
        
        # find position to pivot  list == list length - modded k - 1
        for i in range(length - k - 1):
            # for each iteration move to next postion in linked list
            cur = cur.next
        
        # the new head of the rotated linked list will be the next value of the current node
        newHead = cur.next
        # update the next value of the current node to null as it is now the end of the linked list
        cur.next = None
        # set tail.next to the beginning of the linked list
        tail.next = head
        
        # return rotated linked list
        # solution is linear time O(N)
        return newHead


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # head: List(int),  k: int, output: list(int)
        ([1,2,3,4,5],       2,      [4,5,1,2,3]),
        ([0,1,2],           4,      [2,0,1]),
    )

    mySolution = Solution()

    for head, k, expected in INPUTS:
        continue  # delete, see TODO below

        # TODO: convert list input to linked list
        # code will fail if input not linked list

        print(f"head: {head}, k: {k}")
        actual = mySolution.rotateRight(head, k)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
