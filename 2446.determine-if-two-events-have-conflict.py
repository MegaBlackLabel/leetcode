#
# @lc app=leetcode id=2446 lang=python3
#
# [2446] Determine if Two Events Have Conflict
#

# @lc code=start
from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
         return not (event1[1] < event2[0] or event1[0] > event2[1])
# @lc code=end

