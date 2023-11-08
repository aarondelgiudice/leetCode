"""153. Find Minimum in Rotated Sorted Array | Medium"""

import time

from typing import List


def main():
    TEST_CASES = (
        # nums              expected
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    )

    success = 0
    start_time = time.time()

    for nums, expected in TEST_CASES:
        current_start_time = time.time()

        actual = solution(nums)

        current_end_time = time.time()
        current_total_time = round(current_end_time - current_start_time, 4)

        if actual == expected:
            print(f"✅ solution({nums}) returned {actual}. Took {current_total_time}s.")

            success += 1

        else:
            print(f"❌ solution({nums}) returned {actual}, but expected {expected}")

    end_time = time.time()
    total_time = round(end_time - start_time, 4)

    assert success == len(TEST_CASES), f"❌ {len(TEST_CASES)-success} test(s) failed."

    print(f"\n✅ {success} test(s) passed! Took {total_time}s.")

    return


def solution(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[left] < nums[right]:
            # array is sorted -> return nums[left]
            break

        # check if nums[mid:right] is ascending or descending
        if nums[mid] >= nums[right]:
            # nums[mid:right] is descending -> so ignore left half of array
            left = mid + 1  # increment left pointer

        else:
            # nums[mid] < nums[right]
            # nums[mid:right] is ascending -> so ignore right half of array
            right = mid - 1  # decrement right pointer

    return nums[left]


if __name__ == "__main__":
    main()
