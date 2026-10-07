#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
import math


class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        non_covered_count = 0

        max_end_point = -math.inf
      
        for start, end in intervals:
            if end > max_end_point:
                non_covered_count += 1
                max_end_point = end
      
        return non_covered_count
# @lc code=end

