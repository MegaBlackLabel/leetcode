#
# @lc app=leetcode id=1560 lang=python3
#
# [1560] Most Visited Sector in  a Circular Track
#

# @lc code=start
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]
    
        if start <= end:
            return range(start, end + 1)
        
        return list(range(1, end + 1)) + list(range(start, n + 1))
# @lc code=end

