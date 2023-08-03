#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max = 0
        secondMax = 0

        for i, num in enumerate(nums):
            if num > max:
                secondMax = max
                max = num
                ans = i
            elif num > secondMax:
                secondMax = num

        return ans if max >= 2 * secondMax else -1
# @lc code=end

