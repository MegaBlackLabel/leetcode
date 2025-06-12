#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)

    def pickIndex(self) -> int:

      
        target = random.randint(1, self.prefix_sum[-1])
        
        left, right = 0, len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

