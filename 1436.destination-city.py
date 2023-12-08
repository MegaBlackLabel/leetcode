#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
import collections
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        count = collections.Counter()

        for a, b in paths:
            count[a] += 1

        for a, b in paths:
            if b in count:
                count[b] -= 1
                if count[b] == 0:
                    del count[b]
            else:
                return b
# @lc code=end

