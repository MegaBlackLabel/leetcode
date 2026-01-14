#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#

# @lc code=start
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        powerful_ints = set()

        x_powers = [1]
        if x > 1:
            while x_powers[-1] * x <= bound:
                x_powers.append(x_powers[-1] * x)

        y_powers = [1]
        if y > 1:
            while y_powers[-1] * y <= bound:
                y_powers.append(y_powers[-1] * y)

        for x_power in x_powers:
            for y_power in y_powers:
                total = x_power + y_power
                if total <= bound:
                    powerful_ints.add(total)
                else:
                    break

        return list(powerful_ints)
# @lc code=end

