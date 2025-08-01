#
# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#

# @lc code=start
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        
        n = min(n, 3)

        if presses == 0:
            return 1
        if presses == 1:
            return [2, 3, 4][n - 1]
        if presses == 2:
            return [2, 4, 7][n - 1]

        return [2, 4, 8][n - 1]
        

# @lc code=end

