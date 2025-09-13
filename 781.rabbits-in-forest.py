#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

# @lc code=start
import collections
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        count = collections.Counter(answers)
        result = 0

        for x, freq in count.items():
            group_size = x + 1
            groups = (freq + group_size - 1) // group_size
            result += groups * group_size

        return result
# @lc code=end

