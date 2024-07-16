#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
from heapq import heapify, heapreplace
from math import sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        min_heap = [-gift for gift in gifts]
        heapify(min_heap)
      
        for _ in range(k):
            heapreplace(min_heap, -int(sqrt(-min_heap[0])))
      
        return -sum(min_heap)
# @lc code=end

