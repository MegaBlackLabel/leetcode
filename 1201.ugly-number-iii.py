#
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#

# @lc code=start
import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = math.lcm(a, b)
        bc = math.lcm(b, c)
        ac = math.lcm(a, c)
        abc = math.lcm(ab, c)
        
        def count(x: int) -> int:
            return (x // a + x // b + x // c) - (x // ab + x // bc + x // ac) + (x // abc)
        
        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1
                
        return left
# @lc code=end

