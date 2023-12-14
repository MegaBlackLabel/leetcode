#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Subarrays
#

# @lc code=start
import collections
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(arr) == collections.Counter(target)
# @lc code=end

