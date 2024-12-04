#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]

        for i in range(n):
            for j in reversed(range(len(ans))):
                ans.append(ans[j] | 1 << i)

        return ans
# @lc code=end

