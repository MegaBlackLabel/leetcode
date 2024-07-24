#
# @lc app=leetcode id=2591 lang=python3
#
# [2591] Distribute Money to Maximum Children
#

# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1

        count7 = money // 7
        remaining = money % 7

        if count7 == children and remaining == 0:
            return count7

        if count7 == children - 1 and remaining == 3:
            return count7 - 1

        return min(children - 1, count7)
# @lc code=end

