#
# @lc app=leetcode id=3206 lang=python3
#
# [3206] Alternating Groups I
#

# @lc code=start
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        
        for i in range(n):
            if colors[i-1] != colors[i] and colors[i] != colors[(i+1) % n]:
                count += 1
                
        return count
# @lc code=end

