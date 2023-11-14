"""349. Intersection of Two Arrays | Easy"""

from typing import List


def main():
    TEST_CASES = (([1, 2, 2, 1], [2, 2], [2]), ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]))

    success = 0

    for nums1, nums2, expected in TEST_CASES:
        actual = solution(nums1, nums2)

        if sorted(actual) == sorted(expected):
            print(f"✅ solution({nums1}, {nums2}) returned {actual}")
            success += 1

        else:
            print(
                f"❌ solution({nums1}, {nums2}) returned {actual}, but expected {expected}"
            )

    if success == len(TEST_CASES):
        print(f"\n✅ {success} test(s) passed!")

    else:
        raise AssertionError(f"❌ {len(TEST_CASES)-success} test(s) failed")

    return


def solution(nums1: List[int], nums2: List[int]) -> List[int]:
    # binary search + merge sort solution
    # we want to use index lookup in the longer array and binary search in the sorter array
    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1

    # we only need to sort the smaller of the two arrays (for binary search)
    nums2 = merge_sort(nums2)

    # loop over the longer array (index lookup)
    intersection = set()
    i = 0

    while i < len(nums1):
        if binary_search(nums2, nums1[i]) != -1:
            intersection.add(nums1[i])
            nums1.pop(i)

        else:
            i += 1

    return list(intersection)

    # theoretically slower solution because it uses list search vs. binary search
    # convert lists to sets -> remove duplicates
    nums1, nums2 = list(set(nums1)), list(set(nums2))

    # set nums1 as the longer of two lists
    # loop over the longer list and search in the shorter list
    # loop (index) -> O(1) vs. list search -> O(n)
    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1

    intersection = set()

    i = 0
    while i < len(nums1):
        # check if element in nums1 is in intersection
        # (either in nums2 or intersection)
        if (nums1[i] in nums2) or (nums1[i] in intersection):
            # for either case, pop element from nums1
            intersection.add(nums1[i])
            nums1.pop(i)

        else:
            # otherwise, continue searching nums1
            i += 1

    return list(intersection)


# helper functions
def merge_sort(arr: List) -> List:
    # base case: array is empty or has one element
    if not arr or len(arr) <= 1:
        # array does not need to be sorted -> return array
        return arr

    else:
        # recursive case: array has more than one element
        # split array into two halves and recursively sort each half
        pivot = len(arr) // 2
        left = merge_sort(arr[:pivot])
        right = merge_sort(arr[pivot:])

        # merge sorted halves
        l, r = 0, 0
        merged = []

        while (l < len(left)) and (r < len(right)):
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1

            else:
                merged.append(right[r])
                r += 1

        # add remaining elements from left and right halves
        merged += left[l:]
        merged += right[r:]

        return merged


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if target > nums[mid]:
            left = mid + 1

        elif target < nums[mid]:
            right = mid - 1

        else:
            # target == nums[mid]
            return mid

    return -1


if __name__ == "__main__":
    main()
