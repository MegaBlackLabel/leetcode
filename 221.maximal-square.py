#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * n
        maxLength = 0
        prev = 0

        for i in range(m):
            for j in range(n):
                cache = dp[j]
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    dp[j] = 1 if matrix[i][j] == '1' else 0
                else:
                    dp[j] = min([prev, dp[j], dp[j - 1]]) + 1
                maxLength = max(maxLength, dp[j])
                prev = cache

        return maxLength * maxLength
# @lc code=end

