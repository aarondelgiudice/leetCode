"""69. Sqrt(x) | easy"""


def main(**args):
    # test cases
    TEST_CASES = (
        # (x, expected)
        (4, 2),
        (8, 2),
        (9, 3),
        (10, 3),
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (5, 2),
        (6, 2),
        (7, 2),
        (2147395599, 46339),
    )

    success = 0

    for x, expected in TEST_CASES:
        actual = solution(x)

        if actual == expected:
            print(f"✅ solution({x}) returned {actual}")
            success += 1

        else:
            print(f"❌ solution({x}) returned {actual}, but expected {expected}")

    if success == len(TEST_CASES):
        print(f"\n✅ {success} test(s) passed!")

    else:
        raise AssertionError(f"❌ {len(TEST_CASES)-success} test(s) failed")

    return


def solution(x: int) -> int:
    # binary search -> keep increasing left until mid*mid > x
    left, right = 0, x

    sqrt = left

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid == x:
            return mid

        elif mid * mid < x:
            sqrt = mid
            left = mid + 1

        else:
            # mid * mid > x
            right = mid - 1

    return sqrt


if __name__ == "__main__":
    main()
