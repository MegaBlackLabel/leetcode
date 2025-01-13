#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        dpMin = nums[0] 
        dpMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prevMin = dpMin     
            prevMax = dpMax     
            if num < 0:
                dpMin = min(prevMax * num, num)
                dpMax = max(prevMin * num, num)
            else:
                dpMin = min(prevMin * num, num)
                dpMax = max(prevMax * num, num)

            ans = max(ans, dpMax)

        return ans
# @lc code=end

