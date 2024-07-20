#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        leftSum = 0
        rightSum = sum(nums)

        for num in nums:
            rightSum -= num
            ans.append(abs(leftSum - rightSum))
            leftSum += num

        return ans
# @lc code=end

