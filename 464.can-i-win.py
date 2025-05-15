#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        if desiredTotal <= 0:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        memo = {}

        def canWin(used, total):
            if used in memo:
                return memo[used]
            for i in range(maxChoosableInteger):
                if (used >> i) & 1 == 0:
                    if total + i + 1 >= desiredTotal or not canWin(used | (1 << i), total + i + 1):
                        memo[used] = True
                        return True
            memo[used] = False
            return False

        return canWin(0, 0)
# @lc code=end

