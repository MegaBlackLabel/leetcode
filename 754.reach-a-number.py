#
# @lc app=leetcode id=754 lang=python3
#
# [754] Reach a Number
#

# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)
        step = 0
        total = 0

        while total < target or (total - target) % 2 != 0:
            step += 1
            total += step

        return step
# @lc code=end

