#
# @lc app=leetcode id=3216 lang=python3
#
# [3216] Lexicographically Smallest String After a Swap
#

# @lc code=start
import itertools


class Solution:
    def getSmallestString(self, s: str) -> str:
        chars = list(s)
        for i, (a, b) in enumerate(itertools.pairwise(chars)):
            if ord(a) % 2 == ord(b) % 2 and a > b:
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
                return "".join(chars)
        
        return s
# @lc code=end

