#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        max_length = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            max_length = max(max_length, dp[i])
        total_count = 0
        for i in range(n):
            if dp[i] == max_length:
                total_count += count[i]
        return total_count  
# @lc code=end

