#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = length = 0
        for c in s:
            if c == 'L':
                length += 1
            else:
                length -= 1
            if length == 0:
                ans += 1
        return ans
# @lc code=end

