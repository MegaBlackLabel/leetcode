#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1 - n, n, 2))
# @lc code=end

