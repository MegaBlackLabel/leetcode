#
# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#

# @lc code=start
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        ans = list(range(1, n - k + 1))

        for i in range(k):
            if i % 2 == 0:
                ans.append(n - i // 2)
            else:
                ans.append(n - k + (i + 1) // 2)

        return ans
# @lc code=end

