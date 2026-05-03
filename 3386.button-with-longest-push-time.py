#
# @lc app=leetcode id=3386 lang=python3
#
# [3386] Button with Longest Push Time
#

# @lc code=start
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ans_index = events[0][0]
        max_duration = events[0][1]
        prev_time = events[0][1]
        
        for i in range(1, len(events)):
            idx, current_time = events[i]
            duration = current_time - prev_time
            
            if duration > max_duration:
                max_duration = duration
                ans_index = idx
            elif duration == max_duration:
                if idx < ans_index:
                    ans_index = idx
            
            prev_time = current_time
            
        return ans_index
# @lc code=end

