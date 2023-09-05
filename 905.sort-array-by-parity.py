#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = 0
        r = len(nums) - 1

        while length < r:
            if nums[length] % 2 == 1 and nums[r] % 2 == 0:
                nums[length], nums[r] = nums[r], nums[length]
            if nums[length] % 2 == 0:
                length += 1
            if nums[r] % 2 == 1:
                r -= 1

        return nums
# @lc code=end

