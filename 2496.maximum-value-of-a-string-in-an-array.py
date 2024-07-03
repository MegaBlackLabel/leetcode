#
# @lc app=leetcode id=2496 lang=python3
#
# [2496] Maximum Value of a String in an Array
#

from typing import List

# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(len(s) if any(c.isalpha() for c in s) else int(s) for s in strs)
# @lc code=end

