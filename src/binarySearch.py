"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

source: https://leetcode.com/problems/binary-search/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) solution
        # set left, right pointers
        l, r = 0, len(nums)-1

        # if left pointer > right pointer,
        # then the pointers have crossed
        # and we have search all elements in the array        
        while l <= r:
            # set the mid point (taking the floor vs. ceiling)
            mid = (l + r) // 2

            if nums[mid] > target:
                # disregard all elements in nums that are greater than target
                r = mid - 1

            elif nums[mid] < target:
                # disregard all elements in nums that are less than target
                l = mid + 1 

            else:  # nums[mid] == target:
                return mid

        return -1


if __name__ == "__main__":
    INPUTS = (
        # input: List[int],     int output: int
        ([-1, 0, 3, 5, 9, 12],  9,  4),
        ([-1, 0, 3, 5, 9, 12],  2,  -1),
    )

    for input, target, expected in INPUTS:
        actual = Solution().search(input, target)
        assert actual == expected, f"{input=}, {target=}, {expected=}, {actual=}"
