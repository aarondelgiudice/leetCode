"""
2529. Maximum Count of Positive Integer and Negative Integer

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the
number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then
return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

Constraints:
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
"""

from typing import List

def main():
    TEST_CASES = (
        # nums                  expected
        ([-2,-1,-1,1,2,3],      3),
        ([-3,-2,-1,0,0,1,2],    3),
        ([5,20,66,1314],        4),
    )

    for nums, expected in TEST_CASES:
        actual = Solution().maximumCount(nums)
        assert actual == expected, f"{expected=}, {actual=}"

    return

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # binary search solution: O(log n) time, O(1) space
        def _bisect_left(nums: List[int], target: int=0) -> int:
            # NOTE: python already includes a bisect_left function, but where's the fun in that?
            # NOTE: usually binary search requires right pointer to be right = len(nums)-1
            left, right = 0, len(nums)

            while left < right:
                mid = (left+right)//2

                if nums[mid] < target:
                    left = mid + 1

                else: # nums[mid] >= target
                    right = mid

            return left # count of values left of target

        neg = _bisect_left(nums, 0)
        pos = len(nums) - _bisect_left(nums, 1)

        return max(pos, neg)

        # linear solution: O(n) time, O(1) space
        pos, neg = 0, 0

        for num in nums:
            if num > 0:
                pos += 1

            elif num < 0:
                neg += 1

        return max(pos, neg)

if __name__ == "__main__":
    main()
