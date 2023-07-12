#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


# @lc code=end
