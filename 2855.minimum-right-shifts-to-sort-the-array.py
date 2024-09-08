#
# @lc app=leetcode id=2855 lang=python3
#
# [2855] Minimum Right Shifts to Sort the Array
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        count = 0

        for i, (a, b) in enumerate(itertools.pairwise(nums)):
            if a > b:
                count += 1
                pivot = i

        if count == 0:
            return 0
        if count > 1 or nums[-1] > nums[0]:
            return -1
        return len(nums) - pivot - 1
# @lc code=end

