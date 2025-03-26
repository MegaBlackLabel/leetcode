#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                dp[lo][hi] = min(x + max(dp[lo][x - 1], dp[x + 1][hi]) for x in range(lo, hi))
        
        return dp[1][n]
# @lc code=end

