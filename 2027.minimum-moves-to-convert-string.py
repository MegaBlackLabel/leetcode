#
# @lc app=leetcode id=2027 lang=python3
#
# [2027] Minimum Moves to Convert String
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0

        i = 0
        while i < len(s):
            if s[i] == 'O':
                i += 1
            else:
                ans += 1
                i += 3

        return ans
# @lc code=end

