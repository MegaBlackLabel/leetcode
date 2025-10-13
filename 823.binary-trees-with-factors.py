#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr.sort()
        index = {x: i for i, x in enumerate(arr)}
        dp = [1] * len(arr)
        mod = 10**9 + 7

        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    right = x // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= mod

        return sum(dp) % mod
# @lc code=end

