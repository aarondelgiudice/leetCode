""" 33. Search in Rotated Sorted Array | Medium """
import pytest

from typing import List


def main():
    TEST_CASES = (
        # nums, target, expected
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    )

    success = 0

    for nums, target, expected in TEST_CASES:
        actual = solution(nums, target)

        if actual == expected:
            print(f"✅ solution({nums}, {target}) returned {actual}")
            success += 1
        else:
            print(
                f"❌ solution({nums}, {target}) returned {actual}, but expected {expected}"
            )

    if success == len(TEST_CASES):
        print(f"\n✅ {success} test(s) passed!")

    else:
        raise AssertionError(f"❌ {len(TEST_CASES)-success} test(s) failed")

    return


def solution(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:
            # nums[left:mid] is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1

            else:
                left = mid + 1

        # elif nums[mid] <= nums[right]:
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1

            else:
                right = mid - 1

    return -1  # no solution found


if __name__ == "__main__":
    main()
