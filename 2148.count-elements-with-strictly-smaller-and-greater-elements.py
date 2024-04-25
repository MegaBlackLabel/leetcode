#
# @lc app=leetcode id=2148 lang=python3
#
# [2148] Count Elements With Strictly Smaller and Greater Elements 
#

# @lc code=start
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        
        return sum(mini < num < maxi for num in nums)
# @lc code=end

