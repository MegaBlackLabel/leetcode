#
# @lc app=leetcode id=3168 lang=python3
#
# [3168] Minimum Number of Chairs in a Waiting Room
#

# @lc code=start
class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        chairs = 0
        for c in s:
            chairs += 1 if c == 'E' else -1
            ans = max(ans, chairs)
        return ans
# @lc code=end

