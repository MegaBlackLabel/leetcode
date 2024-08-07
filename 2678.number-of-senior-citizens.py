#
# @lc app=leetcode id=2678 lang=python3
#
# [2678] Number of Senior Citizens
#

# @lc code=start
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(detail[11:13]) > 60 for detail in details)
# @lc code=end

