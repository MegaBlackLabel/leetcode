#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            
            nums[idx] *= multiplier
            
            heapq.heappush(heap, (nums[idx], idx))
            
        return nums
# @lc code=end

