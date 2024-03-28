#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
import collections
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
        
        return sum(count[i] * count[i - k] for i in range(k + 1, 101))
    
# @lc code=end

