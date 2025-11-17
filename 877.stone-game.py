#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i, pile in enumerate(piles):
            dp[i][i] = pile

        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                dp[i][j] = max(piles[i] - dp[i + 1][j],
                               piles[j] - dp[i][j - 1])
        
        return dp[0][n - 1] > 0

# @lc code=end

