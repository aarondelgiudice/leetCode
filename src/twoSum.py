"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

source: https://leetcode.com/problems/two-sum/
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## brute force
        ## time complexity: O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue

        #         if nums[i]+nums[j] == target:
        #             return [i, j]

        # hashmap
        # time complexity O(n)
        # if A + B = target then A = target - B
        sums = {}
        for i , num in enumerate(nums):
            # find target - B
            diff = target - num
            
            # if target - B in sums then i == A
            if diff in sums:
                return [sums[diff] , i]
            
            # else add B to sums
            # and continue to the next value in the nums
            else:
                sums[num] = i
        
        return # no solution found      

if __name__ == "__main__":
    INPUTS = (
    # nums: List(int),  target: int,    output: list(int)
    ([2,7,11,15],       9,              [0,1]),
    ([3,2,4],           6,              [1,2]),
    ([3,3],             6,              [0,1]),
    )

    mySolution = Solution()

    for nums, target, expected in INPUTS:
        print(f"nums: {nums}, target: {target}")
        actual = mySolution.twoSum(nums=nums, target=target)
        print(f"actual: {actual}, expected: {expected}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
