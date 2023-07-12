#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#


# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0


# @lc code=end
