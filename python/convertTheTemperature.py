"""
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature
in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

Note that:
Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00

Example 1:
Input: celsius = 36.50
Output: [309.65000,97.70000]
Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

Example 2:
Input: celsius = 122.11
Output: [395.26000,251.79800]
Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.

Constraints:
0 <= celsius <= 1000

source: https://leetcode.com/problems/convert-the-temperature/
"""

from typing import List

class Solution:
    def c2k(self, c: float) -> float:
        return c + 273.15
    def c2f(self, c: float) -> float:
        return c*1.8 + 32
    def convertTemperature(self, celsius: float) -> List[float]:
        return (self.c2k(celsius), self.c2f(celsius))

if __name__ == "__main__":
    INPUTS = (
        # celsius   expected
        (36.50,     [309.65000,97.70000]),
        (122.11,    [395.26000,251.79800]),
    )

    for celsius, expected in INPUTS:
        actual = Solution().convertTemperature(celsius)
        assert actual == expected, f"{celsius=}, {expected=}, {actual=}"
