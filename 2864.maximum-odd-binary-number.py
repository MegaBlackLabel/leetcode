#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return '1' * (s.count('1') - 1) + '0' * s.count('0') + '1'
# @lc code=end

