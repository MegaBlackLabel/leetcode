#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#

# @lc code=start
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for A in range(n):
            B = n - A
            if '0' not in str(A) and '0' not in str(B):
                return A, B
# @lc code=end

