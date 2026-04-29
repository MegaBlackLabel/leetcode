#
# @lc app=leetcode id=3370 lang=python3
#
# [3370] Smallest Number With All Set Bits
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1
# @lc code=end

