#
# @lc app=leetcode id=1876 lang=python3
#
# [1876] Substrings of Size Three with Distinct Characters
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0

        for a, b, c in zip(s, s[1:], s[2:]):
            if a == b or a == c or b == c:
                continue
            ans += 1

        return ans
# @lc code=end

