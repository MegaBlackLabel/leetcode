#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
import bisect


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        len = bisect.bisect_left(range(num), num, key=lambda m: m * m)
        return len**2 == num


# @lc code=end
