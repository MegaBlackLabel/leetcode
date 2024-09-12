#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#

# @lc code=start
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        maxDiff = 0 
        maxNum = 0 

        for num in nums:
            ans = max(ans, maxDiff * num)         # num := nums[k]
            maxDiff = max(maxDiff, maxNum - num)  # num := nums[j]
            maxNum = max(maxNum, num)             # num := nums[i]

        return ans
# @lc code=end

