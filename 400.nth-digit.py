#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        
        digit = 1
        count = 9
        start = 1
        
        while n > digit * count:
            n -= digit * count
            digit += 1
            count *= 10
            start *= 10
        
        start += (n - 1) // digit
        num_str = str(start)
        
        return int(num_str[(n - 1) % digit])
# @lc code=end

