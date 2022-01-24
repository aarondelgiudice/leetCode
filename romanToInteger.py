"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

source: leetcode.com/problems/roman-to-integer/
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I"     : 1,
            "IV"    : 4,
            "V"     : 5,
            "IX"    : 9,
            "X"     : 10,
            "XL"    : 40,
            "L"     : 50,
            "XC"    : 90,
            "C"     : 100,
            "CD"    : 400,
            "D"     : 500,
            "CM"    : 900,
            "M"     : 1000,
        }

        seq = list(romans.keys())[::-1]  # e.g. ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        stack = []

        i = 0
        while i < len(s):
            char = s[i]

            for numeral in seq:
                char = s[i:i+len(numeral)]

                if char == numeral:
                    stack.append(romans[char])

                    i += len(numeral)

        return sum(stack)


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # input: str,   output: int
        ("III",         3),
        ("LVIII",       58),
        ("MCMXCIV",     1994)
    )

    mySolution = Solution()

    for roman, expected in INPUTS:
        print(f"input: {roman}")
        actual = mySolution.romanToInt(roman)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
