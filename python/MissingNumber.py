""" 268. Missing Number | Easy """

import time
import sys
from typing import List


def main(args):
    # test cases
    TEST_CASES = (
        # (nums, expected)
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
    )

    success = 0
    start_time = time.time()

    for nums, expected in TEST_CASES:
        current_start_time = time.time()
        actual = solution(nums)
        current_end_time = time.time()
        current_total_time = round(current_end_time - current_start_time, 4)

        if actual == expected:
            print(f"✅ solution({nums=}) returned {actual}. Took {current_total_time}s")
            success += 1

        else:
            print(
                f"❌ solution({nums=}) returned {actual}, but expected {expected}. Took {current_total_time}s"
            )

    end_time = time.time()
    total_time = round(end_time - start_time, 4)

    assert success == len(TEST_CASES), f"❌ {len(TEST_CASES)-success} test(s) failed"

    print(f"\n✅ {success} test(s) passed! Took {total_time}s.")

    return


def solution(nums: List[int]) -> int:
    # gaus formula -> O(n) time complexity, O(1) space complexity
    # (n * (n+1))/2 where `n` is the length of input `nums`
    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)

    # binary search solution -> O(nlogn) time complexity, O(1) space complexity
    nums = merge_sort(nums)

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == mid:
            left = mid + 1

        else:
            right = mid - 1

    return left


def merge_sort(arr: List) -> List:
    if not arr or len(arr) <= 1:
        return arr

    else:
        pivot = len(arr) // 2

        left = arr[:pivot]
        right = arr[pivot:]

        left = merge_sort(left)
        right = merge_sort(right)

        i = 0
        j = 0

        merged = []

        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                merged.append(left[i])

                i += 1

            else:
                # left[i] > right[j]
                merged.append(right[j])

                j += 1

        merged += left[i:]
        merged += right[j:]

        return merged


if __name__ == "__main__":
    main(sys.argv[1:])
