#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for a in arr:
            if a * 2 in seen or a % 2 == 0 and a // 2 in seen:
                return True
            seen.add(a)

        return False
# @lc code=end

