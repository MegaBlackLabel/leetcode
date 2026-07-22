#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        total_cost = 0
        
        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                total_cost += mid * min(stack[-1], num)
            stack.append(num)
            
        while len(stack) > 2:
            mid = stack.pop()
            total_cost += mid * stack[-1]
            
        return total_cost
# @lc code=end

