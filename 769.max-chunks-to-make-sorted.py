#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        count = 0
        max_so_far = -1

        for i, num in enumerate(arr):
            max_so_far = max(max_so_far, num)

            if max_so_far == i:
                count += 1

        return count
# @lc code=end

