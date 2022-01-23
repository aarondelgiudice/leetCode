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
        for num1 in nums:
            num2 = target - num1

            num1_idx = nums.index(num1)

            sub_nums = nums.copy()
            sub_nums[num1_idx] = None  # prevent selecting the same index twice

            if num2 in sub_nums:
                num2_idx = sub_nums.index(num2)

                return [num1_idx, num2_idx]        


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
    # nums: List(int),  target: int,    output: list(int)
    ([2,7,11,15],       9,              [0,1]),
    ([3,2,4],           6,              [1,2]),
    ([3,3],             6,              [0,1]),
    )

    mySolution = Solution()

    for nums, target, actual in INPUTS:
        print(f"nums: {nums}, target: {target}")
        expected = mySolution.twoSum(nums=nums, target=target)
        print(f"actual: {actual}, expected: {expected}")
