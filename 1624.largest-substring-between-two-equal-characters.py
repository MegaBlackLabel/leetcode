#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        lastSeen = {}

        for i, c in enumerate(s):
            if c not in lastSeen:
                lastSeen[c] = i
            else:
                ans = max(ans, i - lastSeen[c] - 1)

        return ans
# @lc code=end

