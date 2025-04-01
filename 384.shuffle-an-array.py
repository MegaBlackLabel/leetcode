#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start

import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.original = nums.copy()


    def reset(self) -> List[int]:
        
        return self.original

    def shuffle(self) -> List[int]:
        
        shuffled = self.nums.copy()
        n = len(shuffled)
        
        for i in range(n):
            j = random.randint(i, n - 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        
        return shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

