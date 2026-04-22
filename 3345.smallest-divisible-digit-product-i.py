#
# @lc app=leetcode id=3345 lang=python3
#
# [3345] Smallest Divisible Digit Product I
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_digit_product(num):
            product = 1
            for digit in str(num):
                product *= int(digit)
            return product
        
        # nから順に調べていく
        for num in range(n, n + 20): # 十分な範囲を探索
            if get_digit_product(num) % t == 0:
                return num
        return -1
# @lc code=end

