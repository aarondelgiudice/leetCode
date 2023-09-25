"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

source: https://leetcode.com/problems/contains-duplicate/
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # one liner solution
        # return len(set(nums))!=len(nums)

        # O(n) solution: hashset
        uniques = set()
        for i in nums:
            if i in uniques:
                return True
            uniques.add(i)
        return False
        

if __name__ == "__main__":
    INPUTS = (
        # input: List[int]                  output: bool
        ([1, 2, 3, 1],                      True),
        ([1, 2, 3, 4],                      False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],    True),
    )

    for input, expected in INPUTS:
        actual = Solution().containsDuplicate(input)
        assert actual == expected, f"{input=}, {expected=}, {actual=}"
