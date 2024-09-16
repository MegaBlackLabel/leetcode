#
# @lc app=leetcode id=2908 lang=python3
#
# [2908] Minimum Sum of Mountain Triplets I
#

# @lc code=start
import itertools
import math
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ans = math.inf
        minPrefix = list(itertools.accumulate(nums, min))
        minSuffix = list(itertools.accumulate(reversed(nums), min))[::-1]

        for i, num in enumerate(nums):
            if num > minPrefix[i] and num > minSuffix[i]:
                ans = min(ans, num + minPrefix[i] + minSuffix[i])

        return -1 if ans == math.inf else ans
# @lc code=end

