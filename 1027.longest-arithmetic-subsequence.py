#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        max_length = 0
        
        for i in range(len(nums)):
            dp[i] = {}
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                max_length = max(max_length, dp[i][diff])
                
        return max_length
# @lc code=end

