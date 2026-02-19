#
# @lc app=leetcode id=3019 lang=python3
#
# [3019] Number of Changing Keys
#

# @lc code=start
import itertools


class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        return sum(a.lower() != b.lower() for a, b in itertools.pairwise(s))
# @lc code=end

