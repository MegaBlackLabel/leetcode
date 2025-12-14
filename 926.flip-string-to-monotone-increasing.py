#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        dp = 0
        count1 = 0

        for c in s:
            if c == '0':
                dp = min(dp + 1, count1)
            else:
                count1 += 1

        return dp
# @lc code=end

