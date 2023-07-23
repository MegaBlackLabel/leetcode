#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lists,self.num = [],k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.lists, val)
        if len(self.lists) > self.num: 
            heapq.heappop(self.lists)
        return self.lists[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

