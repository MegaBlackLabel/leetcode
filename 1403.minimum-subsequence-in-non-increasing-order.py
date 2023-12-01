#
# @lc app=leetcode id=1403 lang=python3
#
# [1403] Minimum Subsequence in Non-Increasing Order
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans = []
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        half = sum(nums) // 2

        while half >= 0:
            ans.append(-maxHeap[0])
            half += heapq.heappop(maxHeap)

        return ans
# @lc code=end

