#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        operations = 0
        while target > startValue:
            operations += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
        return operations + (startValue - target)
# @lc code=end

