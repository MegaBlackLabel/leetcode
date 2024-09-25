#
# @lc app=leetcode id=2951 lang=python3
#
# [2951] Find the Peaks
#

# @lc code=start
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1, len(mountain) - 1) if mountain[i - 1] < mountain[i] > mountain[i + 1]]
# @lc code=end

