#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#

# @lc code=start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        
        for num in arr:
            prev = num - difference
            dp[num] = dp.get(prev, 0) + 1

        return max(dp.values())
# @lc code=end

