#
# @lc app=leetcode id=1848 lang=python3
#
# [1848] Minimum Distance to the Target Element
#

# @lc code=start
import math
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = math.inf

        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(i - start))

        return ans
# @lc code=end

