"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
for space complexity analysis.)

source: https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # handle edge cases
        if not nums or len(nums) == 0:
            return
        
        # solve
        # output: list of '1's with length equal to nums
        output = [1] * len(nums)

        # set the value of the ith position in output to the product of all previous values in nums
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums))[::-1]:
            output[i] *= postfix
            postfix *= nums[i]

        return output

if __name__ == "__main__":
    INPUTS = (
        # nums: List[int],  output: list[int]
        ([1,2,3,4],         [24,12,8,6]),
        ([-1,1,0,-3,3],     [0,0,9,0,0]),
    )

    mySolution = Solution()

    for nums, expected in INPUTS:
        print(f"nums: {nums}, output: {actual}")
        actual = mySolution.productExceptSelf(nums)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
    