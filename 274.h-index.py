#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        citations.sort()

        for i, citation in enumerate(citations):
             if citation >= n - i:
                return n - i

        return 0
# @lc code=end

