#
# @lc app=leetcode id=2351 lang=python3
#
# [2351] First Letter to Appear Twice
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = [False] * 26

        for c in s:
            if seen[ord(c) - ord('a')]:
                return c
            seen[ord(c) - ord('a')] = True
    
# @lc code=end

