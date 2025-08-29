#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        digits = list(map(int, str(n)))
        marker = len(digits)
        
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                marker = i
                digits[i - 1] -= 1
        
        for i in range(marker, len(digits)):
            digits[i] = 9
        
        return int(''.join(map(str, digits)))
# @lc code=end

