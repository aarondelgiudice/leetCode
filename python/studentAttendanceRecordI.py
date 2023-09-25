"""
source: https://leetcode.com/problems/student-attendance-record-i/
"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0
        
        for char in s:
            if char == 'A':
                absent_count += 1
                late_count = 0
                if absent_count >= 2:
                    return False
            
            elif char == 'L':
                late_count += 1
                if late_count >= 3:
                    return False
            
            else: # char == 'P':
                late_count = 0
        
        # if absent_count >= 2 or late_count >= 3:
        #     return False
        
        return (absent_count < 2 and late_count < 3)
