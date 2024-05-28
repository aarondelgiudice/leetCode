"""1208. Get Equal Substrings Within Budget | Medium"""

from utils.test_solution import test


def main():
    # test cases
    test_cases = [
        # s, t, maxCost, expected
        (("abcd", "bcdf", 3), 3),
        (("abcd", "cdef", 3), 1),
        (("abcd", "acde", 0), 1),
    ]

    test(test_cases, solution)

    return


def solution(s: str, t: str, maxCost: int) -> int:
    def cost(a: str, b: str) -> int:
        # return abs(ord(a) - ord(b)) # faster, but kinda gimmicky
        alpha = "abcdefghijklmnopqrstuvwxyz"
        return abs(alpha.index(a) - alpha.index(b))

    # sliding window
    # maxLen (int): max length of a substring with a cost less than or equal to `maxCost`.
    # left (int): left pointer of the current substring
    # currCost (int): the cost of converting the current substring from `s` to `t`.
    # right (int): right pointer of the current substring. defined in the for loop.
    maxLen = 0
    currCost = 0
    left = 0

    # increase sliding window to the right
    for right in range(len(s)):
        # (increasing the window) add the cost of the new character to `currCost`
        currCost += cost(s[right], t[right])

        # check maxCost
        if currCost > maxCost:
            # (decreasing the window) remove the cost of the oldest (leftmost) character from `currCost`
            currCost -= cost(s[left], t[left])
            left += 1

        else:
            # update `maxLen` if necessary
            currLen = (right - left) + 1
            maxLen = max(maxLen, currLen)

        # increment `right` pointer automatically

    return maxLen


if __name__ == "__main__":
    main()
