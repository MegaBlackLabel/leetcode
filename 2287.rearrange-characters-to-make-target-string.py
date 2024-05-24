#
# @lc app=leetcode id=2287 lang=python3
#
# [2287] Rearrange Characters to Make Target String
#

# @lc code=start
import collections


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        countS = collections.Counter(s)
        countT = collections.Counter(target)
        return min(countS[c] // countT[c] for c in target)
# @lc code=end

