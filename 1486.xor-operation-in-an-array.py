#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
import functools
import operator


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(operator.xor, [start + 2 * i for i in range(n)])
# @lc code=end

