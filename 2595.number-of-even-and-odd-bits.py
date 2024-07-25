#
# @lc app=leetcode id=2595 lang=python3
#
# [2595] Number of Even and Odd Bits
#

# @lc code=start
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0] * 2
        i = 0

        while n > 0:
            ans[i] += n & 1
            n >>= 1
            i ^= 1

        return ans
# @lc code=end

