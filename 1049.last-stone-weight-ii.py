#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:  # noqa: F821
        total_sum = sum(stones)
        target = total_sum // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for stone in stones:
            for j in range(target, stone - 1, -1):
                if dp[j - stone]:
                    dp[j] = True
        
        s1 = 0
        for j in range(target, -1, -1):
            if dp[j]:
                s1 = j
                break
                
        return total_sum - 2 * s1
# @lc code=end

