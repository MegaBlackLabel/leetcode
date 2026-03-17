#
# @lc app=leetcode id=3158 lang=python3
#
# [3158] Find the XOR of Numbers Which Appear Twice
#

# @lc code=start
import collections
import functools
import operator
from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count_map = collections.Counter(nums)
    
        duplicates = [num for num, freq in count_map.items() if freq == 2]
    
        result = functools.reduce(operator.xor, duplicates, 0)
    
        return result

# @lc code=end

