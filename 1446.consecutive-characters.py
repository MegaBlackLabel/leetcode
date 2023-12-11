#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        count = 1

        for i in range(1, len(s)):
            count = count + 1 if s[i] == s[i - 1] else 1
            ans = max(ans, count)

        return ans
    
# @lc code=end

