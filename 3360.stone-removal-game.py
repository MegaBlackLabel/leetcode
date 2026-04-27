#
# @lc app=leetcode id=3360 lang=python3
#
# [3360] Stone Removal Game
#

# @lc code=start
class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        turns = 0
        
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            turns += 1
            
        return turns % 2 == 1
# @lc code=end

