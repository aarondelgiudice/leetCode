"""
852. Peak Index in a Mountain Array

An array arr a mountain if the following properties hold:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1
"""

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # base case(s)
        if not arr: return None
        if len(arr) <= 1: return 0

        # optimal solution: binary search
        # initialize left, right pointers
        # update left until peak is found, i.e. left == arr.index(max(arr))
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left + right)//2
            
            if arr[mid] < arr[mid+1]:
                # arr values are increasing
                # therefore the peak has not been found
                # increment left
                left = mid + 1
            else: # arr[mid] >= arr[mid+1]
                # arr values are decreasing or a plateau
                # therefore the peak has been found
                # so decrement right
                right = mid

        # return peak index (left)
        return left
        
        # sub-optimal solution: two pointer
        slow, fast = 0, 1
        while fast < len(arr):
            if arr[slow] <= arr[fast]:
                slow = fast
                fast += 1
            else: # arr[slow] > arr[fast]
                return slow
        return slow

if __name__ == "__main__":
    INPUTS = (
        # arr           # expected
        ([0,1,0],       1),
        ([0,2,1,0],     1),
        ([0,10,5,2],    1),
    )

    for arr, expected in INPUTS:
        actual = Solution().peakIndexInMountainArray(arr)
        assert actual == expected, f"{arr=}, {actual=}, {expected=}"
