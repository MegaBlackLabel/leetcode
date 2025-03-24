#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        def pow(a, b):
            if b == 0:
                return 1
            if b == 1:
                return a % 1337
            return pow(a, b // 2) * pow(a, b - b // 2) % 1337
        
        res = 1
        for i in b:
            res = pow(res, 10) * pow(a, i) % 1337
        return res
# @lc code=end

