#
# @lc app=leetcode id=1619 lang=python3
#
# [1619] Mean of Array After Removing Some Elements
#

# @lc code=start
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        num = len(arr)
      
        s = int(num * 0.05)
        e = int(num * 0.95)
      
        arr.sort()
      
        trimmed = arr[s:e]
        mean = sum(trimmed) / len(trimmed)
      
        return round(mean, 5)
# @lc code=end

