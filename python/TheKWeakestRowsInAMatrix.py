""" 1337. The K Weakest Rows in a Matrix | Easy """

import time
import heapq
import sys
from typing import List


def main(args):
    # test cases
    TEST_CASES = (
        # (mat, k, expected)
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            3,
            [2, 0, 3],
        ),
        ([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2, [0, 2]),
        ([[1, 0], [0, 0], [1, 0]], 2, [1, 0]),
    )

    success = 0
    start_time = time.time()

    for mat, k, expected in TEST_CASES:
        current_start_time = time.time()

        actual = solution(mat, k)

        current_end_time = time.time()
        current_total_time = round(current_end_time - current_start_time, 4)

        if actual == expected:
            print(
                f"✅ solution({mat=}, {k=}) returned {actual}. Took {current_total_time}s."
            )
            success += 1

        else:
            print(
                f"❌ solution({mat=}, {k=}) returned {actual}, but expected {expected}."
            )

    end_time = time.time()
    total_time = round(end_time - start_time, 4)

    assert success == len(TEST_CASES), f"❌ {len(TEST_CASES)-success} test(s) failed."

    print(f"\n✅ {success} test(s) passed! Took {total_time}s.")

    return


def solution(mat: List[List[int]], k: int) -> List[int]:
    # heap solution - > O(mlogm+klogm) time complexity, O(m) space complexity
    min_heap = []

    # create an array of tuples(row strength, index) for each row in mat
    # O(mlogm) time complexity
    for i in range(len(mat)):
        min_heap.append((sum(mat[i]), i))

    # create a min heap
    heapq.heapify(min_heap)

    # use heappop to find the k number of rows with the minimum sum
    # O(klogm) time complexity
    output = []

    for _ in range(k):
        n_soldiers, idx = heapq.heappop(min_heap)
        output.append(idx)

    return output

    # brute force solution
    # loop over the matrix and count the number of soldiers in each row
    # sort the rows by number of soldiers
    # return the first k rows
    # O(m*n*log(m)) time complexity, O(m) space complexity

    # count the number of soldiers in each row
    soldiers = []

    for row in mat:
        soldiers.append(row.count(1))

    # sort the rows by number of soldiers
    # O(m*log(m)) time complexity
    sorted_rows = sorted(range(len(soldiers)), key=lambda i: soldiers[i])

    # return the first k rows
    return sorted_rows[:k]


if __name__ == "__main__":
    main(sys.argv[1:])
