"""875. Koko Eating Bananas | Medium"""

import math

from typing import List


def main():
    # test cases
    test_cases = (
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    )

    for piles, h, expected in test_cases:
        actual = solution(piles, h)

        if actual == expected:
            print(f"✅ solution(piles={piles}, h={h}) returned {actual}")

        else:
            print(
                f"❌ solution(piles={piles}, h={h}) returned {actual}, but expected {expected}"
            )

    return


def solution(piles: List[int], h: int) -> int:
    # binary search
    left = 1  # min speed -> 1 banana/hour
    right = sum(piles)  # max speed -> all bananas in 1 hour

    while left < right:  # <= will cause time limit exceeded
        mid = left + (right - left) // 2

        hours_spent = 0
        for pile in piles:
            hours_spent += math.ceil(pile / mid)

        if hours_spent <= h:
            right = mid
        else:
            # hours_spent > h
            left = mid + 1

    return right

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
