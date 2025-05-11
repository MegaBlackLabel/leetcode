#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        count = 0
        sum_count = {}

        for a in nums1:
            for b in nums2:
                sum_count[a + b] = sum_count.get(a + b, 0) + 1

        for c in nums3:
            for d in nums4:
                count += sum_count.get(-(c + d), 0)

        return count
# @lc code=end

