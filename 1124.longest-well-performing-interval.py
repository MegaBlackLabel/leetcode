#
# @lc app=leetcode id=1124 lang=python3
#
# [1124] Longest Well-Performing Interval
#

# @lc code=start
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_len = 0
        score = 0
        first_seen = {}
        
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            
            if score > 0:
                max_len = i + 1
            else:
                if (score - 1) in first_seen:
                    max_len = max(max_len, i - first_seen[score - 1])
            
            if score not in first_seen:
                first_seen[score] = i
                
        return max_len
# @lc code=end

