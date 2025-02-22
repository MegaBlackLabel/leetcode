#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        return n - bisect.bisect_left(range(n), n, key=lambda m: citations[m] + m)
# @lc code=end

