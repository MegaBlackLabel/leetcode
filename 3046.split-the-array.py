#
# @lc app=leetcode id=3046 lang=python3
#
# [3046] Split the Array
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)
        
        for count in counts.values():
            if count > 2:
                return False
        
        return True
# @lc code=end

