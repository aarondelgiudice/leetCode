"""2486. Append Characters to String to Make Subsequence | Medium"""

from utils.test_solution import test


def main():
    # (s: str, t: str), expected: int
    test_cases = [
        (("coaching", "coding"), 4),
        (("abcde", "a"), 0),
        (("z", "abcde"), 5),
    ]

    test(test_cases, solution)

    return


def solution(s: str, t: str) -> int:
    # O(s)
    longestPrefix = 0

    for char in s:
        if t[longestPrefix] == char:
            longestPrefix += 1

        if longestPrefix >= len(t):
            break

    return len(t) - longestPrefix

    # two pointers
    left = 0
    longestPrefix = 0

    while left < len(s) and longestPrefix < len(t):
        if s[left] == t[longestPrefix]:
            longestPrefix += 1

        left += 1

    return len(t) - longestPrefix


if __name__ == "__main__":
    main()
