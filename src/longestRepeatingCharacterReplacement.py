"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above
operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

Constraints:
1 <= s.length <= 10**5
s consists of only uppercase English letters.
0 <= k <= s.length
"""

TEST_CASES = (
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
)

def main():
    for s, k, expected in TEST_CASES:
        actual = Solution().characterReplacement(s, k)
        assert actual == expected, f"{s=}, {k=}, {expected=}, {actual=}"

    return

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointer solution -> time o(n), space o(m)
        left = 0
        freq = {}
        maxLen = 0

        for right in range(len(s)):
            # add char to frequency dict
            # if char does not exist: insert 1, else: increment by 1
            freq[s[right]] = 1 + freq.get(s[right], 0)

            # Get the length of the current substring and check validity
            # validity -> difference between current substring legnth and maximum character frequency is less than or equal to K
            # i.e. we have replaced <= k letters -> update maxLen
            curLen = right - left + 1
            is_valid = (curLen - max(freq.values())) <= k

            if is_valid:
                maxLen = max(maxLen, curLen)

            # if we have replaced > K letters, then it's time to slide the window
            else:
                # decrement frequency of char at left pointer, then increment pointer
                # decrementing the left pointer char is essentially removing its count from the current substring
                freq[s[left]] -= 1
                left += 1

        return maxLen

if __name__ == "__main__":
    main()