"""
808. Soup Servings

There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of
operations:
1. Serve 100 ml of soup A and 0 ml of soup B,
2. Serve 75 ml of soup A and 25 ml of soup B,
3. Serve 50 ml of soup A and 50 ml of soup B, and
4. Serve 25 ml of soup A and 75 ml of soup B.

When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four
operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we
will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same
time. Answers within 10**-5 of the actual answer will be accepted.

Example 1:
Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same
time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Example 2:
Input: n = 100
Output: 0.71875

Constraints:

0 <= n <= 10**9
"""

class Solution:
    def soupServings(self, n: int) -> float:
        # first define some really big number as a cutoff
        # the likelihood of A depleting first increases as n increases
        # this is because most servings of A are 25 ml larger than B
        # so if n is at or above a given threshold, return 1.0
        # or a 100% likelihood that A will be depleted first
        if n > 5000:
            return 1

        # dp -> recursion w/ cached results
        cache = {}

        def recursive_fn(a: int, b: int):
            if a <= 0 and b <= 0:
                return 0.5

            elif a <= 0:
                return 1.0

            elif b <= 0:
                return 0.0

            if (a, b) not in cache:
                cache[(a, b)] = 0.25 * (
                    recursive_fn(a-100, b)
                    + recursive_fn(a-75, b-25)
                    + recursive_fn(a-50, b-50)
                    + recursive_fn(a-25, b-75)
                )

            return cache[(a, b)]

        return recursive_fn(n, n)
    

if __name__ == "__main__":
    INPUTS = (
        # n     expected
        (50,    0.62500),
        (100,   0.71875),
    )

    for n, expected in INPUTS:
        actual = Solution().soupServings(n)
        assert actual == expected, f"{actual=}, {expected=}"
