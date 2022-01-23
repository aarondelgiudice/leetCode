"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

source: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged = sorted(merged)

        if len(merged) % 2 == 0:  # len(merged) is odd
            idx1 = int((len(merged) - 1) / 2)
            idx2 = int((len(merged) + 1) / 2)
            return (merged[idx1] + merged[idx2]) / 2
        
        elif len(merged) % 2 != 0:  # len(merged) is even
            idx = int(len(merged) / 2)
            return merged[idx]
        

# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # nums1: List(int), nums2: List(int),   output: float
        ([1,3],             [2],                2.0),
        ([1,2],             [3,4],              2.5),
    )

    mySolution = Solution()

    for nums1, nums2, actual in INPUTS:
        print(f"nums1: {nums1}, nums2: {nums2}")
        expected = mySolution.findMedianSortedArrays(nums1, nums2)
        print(f"expected: {expected}, actual: {actual}")
