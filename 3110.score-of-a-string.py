#
# @lc app=leetcode id=3110 lang=python3
#
# [3110] Score of a String
#

# @lc code=start
from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
    
        ascii_values = map(ord, s)
        score = sum(abs(a - b) for a, b in pairwise(ascii_values))
      
        return score
    
# @lc code=end

