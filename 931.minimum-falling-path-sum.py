#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):
                left = dp[i - 1][j - 1] if j - 1 >= 0 else float('inf')
                up = dp[i - 1][j]
                right = dp[i - 1][j + 1] if j + 1 < n else float('inf')
                dp[i][j] = matrix[i][j] + min(left, up, right)

        return min(dp[-1])
# @lc code=end

