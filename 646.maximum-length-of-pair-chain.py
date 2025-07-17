#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])
        
        current_end = float('-inf')
        count = 0
        
        for start, end in pairs:
            if start > current_end:
                count += 1
                current_end = end
        
        return count
# @lc code=end

