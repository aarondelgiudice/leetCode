"""74. Search a 2D Matrix
Medium
"""

from typing import List


def main():
    # test cases
    testCases = (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    )

    for testCase in testCases:
        matrix, target, expected = testCase
        actual = solution(matrix, target)
        assert (
            actual == expected
        ), f"solution({matrix=}, {target=}) == {actual}, expected {expected}"


def solution(matrix: List[List[int]], target: int) -> bool:
    # better solution: double binary search: rows and col
    # first, binary search rows top -> bottom
    top, bottom = 0, len(matrix) - 1

    while top <= bottom:
        row = top + (bottom - top) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            # target in matrix[row][:]
            break  # store value of variable row

    # next, binary search cols left -> right
    left, right = 0, len(matrix[row]) - 1

    while left <= right:
        col = left + (right - left) // 2

        if target > matrix[row][col]:
            left = col + 1

        elif target < matrix[row][col]:
            right = col - 1

        else:
            # target == matrix[row][col]
            return True

    return False  # no solution found

    # more complicated solution: single binary search -> treat it as a single array
    mRows, nCols = len(matrix), len(matrix[0])
    left, right = 0, mRows * nCols - 1

    while left <= right:
        mid = left + (right - left) // 2

        rowMid = mid // nCols
        colMid = mid % nCols

        if target > matrix[rowMid][colMid]:
            left = mid + 1
        elif target < matrix[rowMid][colMid]:
            right = mid - 1
        else:
            # target == matrix[rowMid][colMid]
            return True

    return False  # no solution found


if __name__ == "__main__":
    main()
