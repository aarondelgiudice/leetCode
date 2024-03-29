"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # easy solution -> heap  -> O(n*logn) time
        # counter
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        priority_queue = []
        for num, freq in frequency.items():
            # map value: -frequency: num
            # note: heapq is a minheap, so convert to negative
            freq *= -1
            heapq.heappush(priority_queue, (freq, num))

        # append the top-k items in priority_queue to result
        result = []
        while priority_queue:
            result.append(heapq.heappop(priority_queue)[1])
            if len(result) ==  k:
                return result

        # better solution -> hashMap -> O(n) time
        counter = {}
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        for key, val in counter.items():
            freq[val].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res

if __name__ == "__main__":
    INPUTS = (
        # nums  k   expected
        ([1,1,1,2,2,3], 2,  [1,2]),
        ([1],           1,  [1]),
    )

    for nums, k, expected in INPUTS:
        actual = Solution().topKFrequent(nums, k)
        assert actual == expected, f"{actual=}, {expected=}, {nums=}, {k=}"
