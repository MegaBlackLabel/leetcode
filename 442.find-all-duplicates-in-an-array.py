#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                result.append(index + 1)
            else:
                nums[index] = -nums[index]
        return result
# @lc code=end

