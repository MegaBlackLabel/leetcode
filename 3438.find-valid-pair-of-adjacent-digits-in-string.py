#
# @lc app=leetcode id=3438 lang=python3
#
# [3438] Find Valid Pair of Adjacent Digits in String
#

# @lc code=start
from typing import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        counts = Counter(s)
        
        for i in range(len(s) - 1):
            d1, d2 = s[i], s[i+1]
            
            if d1 != d2:
                if counts[d1] == int(d1) and counts[d2] == int(d2):
                    return d1 + d2
        
        return ""
# @lc code=end

