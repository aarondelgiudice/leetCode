"""1404. Number of Steps to Reduce a Number in Binary Representation to One | Medium"""

from utils.test_solution import test


def main():
    # test cases
    test_cases = [
        # s, expected
        (("1101",), 6),
        (("10",), 1),
        (("1",), 0),
    ]

    test(test_cases, solution)

    return


def solution(s: str) -> int:
    s = list(s)  # strings are immutable, so convert s to list
    steps = 0

    while len(s) > 1:
        if s[-1] == "0":
            # divide by two
            s.pop()

        else:
            # add one
            i = len(s) - 1

            # first, loop over s right to left
            # set consecutive "1" to a "0"
            while i >= 0 and s[i] != "0":
                s[i] = "0"
                i -= 1

            # finally, set the next element in s to "1"
            if i < 0:
                # if we've looped over all elements in s, insert a "1" at the beginning of s
                s.insert(0, "1")

            else:
                # otherwise, change the element at position `i` to "1"
                s[i] = "1"

        steps += 1

    return steps


if __name__ == "__main__":
    main()
