#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#


# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            return hex(num + (1 << 32))[2:]
        else:
            return hex(num)[2:]


# @lc code=end
