"""
1870. Minimum Speed to Arrive on Time

You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to
the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where
dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on
the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach
the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 10**7 and hour will have at most two digits after the decimal
point.

Example 1:
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3
hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2
hours.
- You will arrive at exactly the 6 hour mark.

Example 2:
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1
hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 =
0.66667 hours.
- You will arrive at the 2.66667 hour mark.

Example 3:
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.

Constraints:
n == dist.length
1 <= n <= 10**5
1 <= dist[i] <= 10**5
1 <= hour <= 10**9
There will be at most two digits after the decimal point in hour.
"""

import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # set the max, min speed as per the problem definition
        minSpeed, maxSpeed = 1, 10**7 + 1
        # set current speed to -1, i.e. no solution
        currSpeed = -1

        # binary search
        while minSpeed <= maxSpeed:
            # find midpoint
            mid = (minSpeed + maxSpeed) // 2

            # determine time to reach destination at speed=mid
            time = 0

            # time_to_destination = distance / speed
            # for each train (expect the final train)
            # round time_to_destination up to the next integer
            # as the next train will only depart at an integer hour
            for i in range(len(dist)-1):
                time += math.ceil(dist[i]/mid)

            # do not round up, as the this is the final train (no next train)
            time += dist[-1]/mid

            # check if time is within threshold (hour)
            if time <= hour:
                # update current speed
                currSpeed = mid
                # decrement max speed as all values greater than currSpeed will statisfy condition
                maxSpeed = mid - 1

            else:
                # the goal is to find the minimum speed,
                # so increment minSpeed until mid does not statisfy the condition time <= hour
                minSpeed = mid + 1

        return currSpeed
    

if __name__ == "__main__":
    INPUTS = (
        ([1, 3, 2], 2.7, 3),
        ([1, 3, 2], 6, 1),
        ([1, 3, 2], 1.9, -1),
        ([1,1,100000], 2.01, 10000000),
    )

    for dist, hour, expected in INPUTS:
        actual = Solution().minSpeedOnTime(dist, hour)
        assert actual == expected, f"{actual=}, {expected=}, {actual==expected}"
