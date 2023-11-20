#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        return arr
    
# @lc code=end

