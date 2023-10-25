#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
import math
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        min = math.inf

        arr.sort()

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min:
                min = diff
                ans = []
            if diff == min:
                ans.append([arr[i], arr[i + 1]])

        return ans
# @lc code=end

