"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 
Constraints:
1 <= k <= 10**4
0 <= nums.length <= 10**4
-10**4 <= nums[i] <= 104
-10**4 <= val <= 10**4
At most 10**4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.

source: https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # solution: minHeap of size k
        # first value in minHeap will always be the kth largest value
        heapq.heapify(nums)
        
        # pop the smallest value until heap is size k
        while len(nums) > k:
            heapq.heappop(nums)
        
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        # add new value to heap
        heapq.heappush(self.nums, val)
    
        # if heap is larger than k, pop the smallest value
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
    
        # find and return the kth largest value
        kth_largest = self.nums[0]
        return kth_largest

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    INPUTS = (
        # nums                                          # expected
        ([[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],  [None, 4, 5, 5, 8, 8]),
    )
    for inputs, expected in INPUTS:
        k = inputs[0][0]
        nums = inputs[0][1]
        kthLargest = KthLargest(k=k, nums=nums)
        for i in range(len(inputs[1:])):
            val = inputs[1:][i][0]
            actual = kthLargest.add(val)
            assert actual == expected[i+1], (actual, expected[i+1])
