"""1002. Find Common Characters | Easy"""

from typing import List, Dict
from utils.test_solution import test


def main():
    # test cases
    test_cases = [
        # words: List[str], output: List[str]
        ((["bella", "label", "roller"],), ["e", "l", "l"]),
        ((["cool", "lock", "cook"],), ["c", "o"]),
    ]

    test(test_cases, solution)

    return


def count_chars(word: str) -> Dict[str, int]:
    counter = {}
    for char in word:
        counter[char] = counter.get(char, 0) + 1
    return counter


def solution(words: List[str]) -> List[str]:
    common = []

    commonCharCounts = count_chars(words[0])

    for i in range(1, len(words)):
        currentCharCounts = count_chars(words[i])

        for char in commonCharCounts.keys():
            commonCharCounts[char] = min(
                commonCharCounts[char], currentCharCounts.get(char, 0)
            )

    for char, count in commonCharCounts.items():
        for _ in range(count):
            common.append(char)

    return common


if __name__ == "__main__":
    main()
