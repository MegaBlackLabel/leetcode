#
# @lc app=leetcode id=3502 lang=python3
#
# [3502] Minimum Cost to Reach Every Position
#

# @lc code=start
from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
      
        result = [0] * n
      
        min_cost_so_far = cost[0]
      
        for index, current_cost in enumerate(cost):
            min_cost_so_far = min(min_cost_so_far, current_cost)
            result[index] = min_cost_so_far
      
        return result
    
# @lc code=end

