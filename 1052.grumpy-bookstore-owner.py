#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        baseline_satisfied = sum(c for c, g in zip(customers, grumpy) if g == 0)
        
      
        additional_satisfied = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_additional = additional_satisfied
        
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
                
            max_additional = max(max_additional, additional_satisfied)
            
        return baseline_satisfied + max_additional
# @lc code=end

