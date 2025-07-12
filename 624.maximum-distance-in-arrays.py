#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#

# @lc code=start
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        if not arrays:
            return 0
        
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_array = arrays[i]
        
            max_distance = max(max_distance, abs(current_array[-1] - min_val), abs(max_val - current_array[0]))

            min_val = min(min_val, current_array[0])
            max_val = max(max_val, current_array[-1])
        
        return max_distance
# @lc code=end

