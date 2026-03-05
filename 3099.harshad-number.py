#
# @lc app=leetcode id=3099 lang=python3
#
# [3099] Harshad Number
#

# @lc code=start
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        s = sum(int(d) for d in str(x))
        
        return s if x % s == 0 else -1
# @lc code=end

