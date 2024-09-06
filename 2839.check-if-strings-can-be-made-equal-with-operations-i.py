#
# @lc app=leetcode id=2839 lang=python3
#
# [2839] Check if Strings Can be Made Equal With Operations I
#

# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def swappedStrings(s: str) -> list[str]:
            chars = list(s)
            return [chars,
              ''.join([chars[2], chars[1], chars[0], chars[3]]),
              ''.join([chars[0], chars[3], chars[2], chars[1]]),
              ''.join([chars[2], chars[3], chars[0], chars[1]])]

        return any(a == b
               for a in swappedStrings(s1)
               for b in swappedStrings(s2))
# @lc code=end

