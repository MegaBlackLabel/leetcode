#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
import functools


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        MOD = 1000000007

        @functools.lru_cache(None)
        def dp(k: int, i: int, j: int) -> int:
            """
            Returns the number of paths to move the ball at (i, j) out-of-bounds with
            k moves.
            """
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if k == 0:
                return 0
            return (dp(k - 1, i + 1, j) + dp(k - 1, i - 1, j) +
              dp(k - 1, i, j + 1) + dp(k - 1, i, j - 1)) % MOD

        return dp(maxMove, startRow, startColumn)
# @lc code=end

