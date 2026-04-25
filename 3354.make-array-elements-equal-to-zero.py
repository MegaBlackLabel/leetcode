#
# @lc app=leetcode id=3354 lang=python3
#
# 
#

# @lc code=start
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        ans = 0
        
        for x in nums:
            if x == 0:
                right_sum = total_sum - left_sum
                if left_sum == right_sum:
                    ans += 2
                elif abs(left_sum - right_sum) == 1:
                    ans += 1
            else:
                left_sum += x
                
        return ans
# @lc code=end

