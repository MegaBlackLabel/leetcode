#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
      
        while numBottles >= numExchange:
            numBottles = numBottles - numExchange + 1
            res += 1
      
        return res
# @lc code=end

