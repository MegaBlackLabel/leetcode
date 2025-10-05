#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#

# @lc code=start
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = prefix_sum[i] / i

        for i in range(1, n + 1):
            for j in range(2, min(i, k) + 1):
                for p in range(j - 1, i):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[p][j - 1] + (prefix_sum[i] - prefix_sum[p]) / (i - p),
                    )

        return dp[n][k]
# @lc code=end

