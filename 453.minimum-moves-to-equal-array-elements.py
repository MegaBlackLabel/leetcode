#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        min_num = min(nums)
        return sum(num - min_num for num in nums)
# @lc code=end

