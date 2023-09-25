"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

source: https://leetcode.com/problems/reverse-linked-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative solution: two pointers
        # time complexity: O(n)
        # memory complexity: O(1)

        # set previous and current pointers
        prev, curr = None, head

        # iterate over listNodes until curr is None (end of list)
        while curr: # is not None
            # create a temp variable for the next listNone (current.next)
            nxt = curr.next
            
            # reverse current postion,
            # replace current.next with previous position
            curr.next = prev
            
            # shift pointers, previous = current, current = next
            prev = curr
            curr = nxt

        # why return prev?
        # curr is set to nxt
        # and nxt is defined by curr.next
        # the final listNote in a linked list will have a head.next value of None
        # so curr == nxt == None
        # so return prev
        return prev

        # # recursive solution:
        # # time complexity: O(n)
        # # memory complexity: O(n)

        def recursion(prev, curr):
            # deal with the base case first
            # if head is null, we are at the end of the linked list
            if curr == None:
                return prev

            # create temp variable to store head
            nxt = curr.next
            # reserve link between curr and prev
            curr.next = prev

            # recursive call
            return recursion(prev=curr, curr=nxt)

        # pass begining of linked list (curr) to recursive function
        return recursion(prev=None, curr=head)


if __name__ == "__main__":
    INPUTS = (
        # input: ListNode,  output: ListNode
        ([1, 2, 3, 4, 5],   [5, 4, 3, 2, 1]),
        ([1, 2],            [2, 1]),
        ([],                []),
    )

    for input, expected in INPUTS:
        actual = Solution().reverseList(input)
        assert actual == expected, f"{input=}, {expected=}, {actual=}"
