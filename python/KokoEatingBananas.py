"""875. Koko Eating Bananas | Medium"""

import math
import time

from typing import List


def main():
    # test cases
    test_cases = (
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    )

    success = 0
    start_time = time.time()

    for piles, h, expected in test_cases:
        current_start_time = time.time()

        actual = solution(piles, h)

        current_end_time = time.time()
        current_total_time = round(current_end_time - current_start_time, 4)

        if actual == expected:
            print(
                f"✅ solution(piles={piles}, h={h}) returned {actual}. Took {current_total_time}s."
            )

            success += 1

        else:
            print(
                f"❌ solution(piles={piles}, h={h}) returned {actual}, but expected {expected}."
            )

    end_time = time.time()
    total_time = round(end_time - start_time, 4)

    assert success == len(test_cases), f"❌ {len(test_cases)-success} test(s) failed."

    print(f"\n✅ {success} test(s) passed! Took {current_total_time}s.")

    return


def solution(piles: List[int], h: int) -> int:
    # binary search
    min_k = 1  # 1 banana/hour
    max_k = max(piles)  # bananas/hour == the largest pile

    while min_k < max_k:
        mid = min_k + (max_k - min_k) // 2

        # time to eat all banans at speed = k
        hours_spent = 0

        for pile in piles:
            hours_spent += math.ceil(pile / mid)

        # check if k is valid
        # we want the max value for k,
        # so keep increasing mid until hours_spent > h
        if hours_spent <= h:
            # hours_spent is valid (but may not optimal yet),
            # so update max_k.
            # the final update to max_k before the while loop
            # exits will be the optimal max_K
            max_k = mid

        else:
            # hours_spent is not valid (hours_spent > h),
            # so increment min_k to increase mid
            min_k = mid + 1

    return max_k  # return optimal k

    # brute force -> will exceed time limit
    # start with minimum value for speed
    speed = 1

    # loop until hours_spent is less than total hours, h
    while True:
        # initialize hours spent
        hours_spent = 0

        # loop over piles and increment hours_spent by time to eat each pile at current speed
        for pile in piles:
            # koko can't eat more than the pile, so use math.ceil to round up the hours variable
            hours_spent += math.ceil(pile / speed)

        # check if hours_spent is valid
        if hours_spent <= h:
            # optimal speed value
            # if speed increases, koko will eat too fast
            # if speed decreases, koko will not finish the banans in time
            return speed

        else:
            # hours_spent > h -> increase speed
            speed += 1


if __name__ == "__main__":
    main()
