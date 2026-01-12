#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#

# @lc code=start
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        if n == 1:
            return [i for i in range(10)]

        result = []

        def backtrack(num: int, length: int) -> None:
            if length == n:
                result.append(num)
                return

            last_digit = num % 10
            next_digits = set()

            if last_digit + k < 10:
                next_digits.add(last_digit + k)
            if last_digit - k >= 0:
                next_digits.add(last_digit - k)

            for next_digit in next_digits:
                backtrack(num * 10 + next_digit, length + 1)

        for starting_digit in range(1, 10):
            backtrack(starting_digit, 1)

        return result
# @lc code=end

