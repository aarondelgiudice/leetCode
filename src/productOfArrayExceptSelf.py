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
        # (easier) prefix, postfix solution -> o(n)
        
        # initialize prefix (left) and postfix (right) arrays
        # with default values of 1 for each position (b/c x*1=x)
        left, right = [1]*len(nums), [1]*len(nums)

        # loop over nums and find the product of all preceding elements (prefix)
        # and proceding elements (postfix)
        for i in range(1, len(nums)):
            left[i] *= left[i-1]*nums[i-1]
            right[-i-1] *= right[-i]*nums[-i]

        # create an empty array to store final output
        # loop over nums a second time and update output array with
        # prefix product * postfix product
        answer = []
        for i in range(len(nums)):
            answer.append(left[i] * right[i])

        return answer        
        # prefix, postfix solution -> o(n)
        # for each position in nums, the product of array except self
        # is equal to prefix*postfix

        # create dummy arrays of 1's
        answer = [1]*len(nums)

        # first loop -> multiply each element in nums by all previous elements
        # product of previous elements is stored in prefix

        # initialize prefix with a default value of 1 (b/c x*1=x)
        prefix = 1

        for i in range(len(nums)):
            # set the current index in answer as prefix
            # AKA the product of all previous elements
            answer[i] = prefix

            # update prefix with the current element in nums
            # (this value will be stored in answer array during the next step of the iteration)
            prefix *= nums[i]

        # second loop -> multiply each element in answer array with postfix value
        # currently answer array contains only the prefix poduct of each element in nums
        # loop through nums in reverse order to update each element in answer array
        # with the postfix product at that current index in nums
        
        # default value of 1
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            # multiply the current position in answer with the current position in postfix
            answer[i] *= postfix

            # update postfix
            # (this value will update the next postion in answer array during the next step of the iteration)
            postfix *= nums[i]
        
        return answer
    
        # # handle edge cases
        # if not nums or len(nums) == 0:
        #     return
        
        # # solve
        # # output: list of '1's with length equal to nums
        # output = [1] * len(nums)

        # # set the value of the ith position in output to the product of all previous values in nums
        # prefix = 1
        # for i in range(len(nums)):
        #     output[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for i in range(len(nums))[::-1]:
        #     output[i] *= postfix
        #     postfix *= nums[i]

        # return output

if __name__ == "__main__":
    INPUTS = (
        # nums,         output
        ([1,2,3,4],     [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    )

    mySolution = Solution()

    for nums, expected in INPUTS:
        actual = mySolution.productExceptSelf(nums)
        assert expected == actual, f"{actual=}, {expected=}"
    