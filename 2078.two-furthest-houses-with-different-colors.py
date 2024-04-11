#
# @lc app=leetcode id=2078 lang=python3
#
# [2078] Two Furthest Houses With Different Colors
#

# @lc code=start
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = 0 
        j = n - 1 
        while colors[i] == colors[-1]:
            i += 1
        while colors[j] == colors[0]:
            j -= 1
        
        return max(n - 1 - i, j)
# @lc code=end

