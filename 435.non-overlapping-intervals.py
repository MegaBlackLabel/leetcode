#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        end = float('-inf')
        
        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                count += 1
        
        return count
# @lc code=end

