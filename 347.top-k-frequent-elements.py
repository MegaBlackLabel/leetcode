#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]

# @lc code=end

