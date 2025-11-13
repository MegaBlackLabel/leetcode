#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        max_length = 0

        for i in range(n):
            for j in range(i + 1, n):
                expected_prev = arr[j] - arr[i]
                if expected_prev < arr[i] and expected_prev in index:
                    k = index[expected_prev]
                    dp[i][j] = dp[k][i] + 1
                    max_length = max(max_length, dp[i][j])

        return max_length if max_length >= 3 else 0    
# @lc code=end

