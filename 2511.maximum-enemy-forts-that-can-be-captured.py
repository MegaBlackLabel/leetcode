#
# @lc app=leetcode id=2511 lang=python3
#
# [2511] Maximum Enemy Forts That Can Be Captured
#

# @lc code=start
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0

        j = 0
        for i, fort in enumerate(forts):
            if fort != 0:
                if fort == -forts[j]:
                    ans = max(ans, i - j - 1)
                j = i

        return ans
# @lc code=end

