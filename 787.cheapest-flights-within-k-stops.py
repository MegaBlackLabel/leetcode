#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dp = [[float('inf')] * n for _ in range(k + 2)]
        dp[0][src] = 0

        for i in range(1, k + 2):
            for u, v, w in flights:
                dp[i][v] = min(dp[i][v], dp[i - 1][u] + w)
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i - 1][j])

        return -1 if dp[k + 1][dst] == float('inf') else dp[k + 1][dst]
# @lc code=end

