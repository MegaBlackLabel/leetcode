#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        return [*map(pattern.index, pattern)] == [*map(t.index, t)]


# @lc code=end
