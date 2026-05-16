#
# @lc app=leetcode id=3442 lang=python3
#
# [3442] Maximum Difference Between Even and Odd Frequency I
#

# @lc code=start
from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s).values()
        
        max_odd = max(f for f in counts if f % 2 != 0)
        min_even = min(f for f in counts if f % 2 == 0)
        
        return max_odd - min_even
# @lc code=end

