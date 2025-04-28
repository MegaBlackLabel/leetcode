#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        start_times = [(interval[0], i) for i, interval in enumerate(intervals)]
        start_times.sort()
        result = []
        
        for interval in intervals:
            left, right = 0, len(start_times) - 1
            while left <= right:
                mid = (left + right) // 2
                if start_times[mid][0] >= interval[1]:
                    right = mid - 1
                else:
                    left = mid + 1
            if left < len(start_times):
                result.append(start_times[left][1])
            else:
                result.append(-1)
        
        return result
# @lc code=end

