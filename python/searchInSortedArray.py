"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or
-1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10**4 <= nums[i] <= 10**4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10**4 <= target <= 10**4
"""

from typing import List

def main():
    TEST_CASES = (
        # nums,             target, expected
        ([4,5,6,7,0,1,2],   0,     4),
        ([4,5,6,7,0,1,2],   3,     -1),
        ([1],               0,     -1),
    )

    for nums, target, expected in TEST_CASES:
        actual = Solution().search(nums, target)
        assert actual == expected, f"{nums=}, {target=}, {expected=}, {actual=}"

    return

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search solution: o(log n)
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            # /normal binary search up until here

            # check if left vs. rght half of array is sorted
            # check left
            if nums[left] <= nums[mid]:
                # if target is in nums[left:mid], then ignore right half of array
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # decrement right pointer

                # else (left half of the array IS sorted, but target is NOT in nums[left:mid]),
                # ignore left half of the array
                else:
                    left = mid + 1 # increment left pointer

            # otherwise, check right half
            else:
                # if target is in nums[mid:right], then ignore the left half of the array
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 # increment left pointer

                # else, (right half of the array IS sorted, but target is NOT in nums[mid:right]),
                # ignore the right half of the array
                else:
                    right = mid - 1 # decrement right pointer

        return -1 # target not found

if __name__ == "__main__":
    main()
