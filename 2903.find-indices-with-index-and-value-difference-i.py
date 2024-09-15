#
# @lc app=leetcode id=2903 lang=python3
#
# [2903] Find Indices With Index and Value Difference I
#

# @lc code=start
from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        minIndex = 0
        maxIndex = 0

        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[minIndex]:
                minIndex = i - indexDifference
            if nums[i - indexDifference] > nums[maxIndex]:
                maxIndex = i - indexDifference
            if nums[i] - nums[minIndex] >= valueDifference:
                return [i, minIndex]
            if nums[maxIndex] - nums[i] >= valueDifference:
                return [i, maxIndex]

        return [-1, -1]
# @lc code=end

