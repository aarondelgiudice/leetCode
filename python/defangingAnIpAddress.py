"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:
The given address is a valid IPv4 address.

source: https://leetcode.com/problems/defanging-an-ip-address/
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # generator
        return "[.]".join(address.split("."))  
        
        # two pointer
        pos = 0 
        while pos < len(address)-1:
            if address[pos] == ".":
                left, right = address[:pos], address[pos+1:]
                address = left + "[.]" + right
                pos += 1
            pos += 1
        return address

if __name__ == "__main__":
    INPUTS = (
        # address           expected
        ("1.1.1.1",         "1[.]1[.]1[.]1"),
        ("255.100.50.0",    "255[.]100[.]50[.]0"),
    )

    for address, expected in INPUTS:
        actual = Solution().defangIPaddr(address)
        assert actual == expected, f"{address=}, {expected=}, {actual=}"

        
