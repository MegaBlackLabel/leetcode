#
# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#

# @lc code=start
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        
        if not nums:
            return ""
        
        n = len(nums)
        
        if n == 1:
            return str(nums[0])
        
        if n == 2:
            return f"{nums[0]}/{nums[1]}"

        result = f"{nums[0]}/(" + "/".join(map(str, nums[1:])) + ")"
        
        return result
# @lc code=end

