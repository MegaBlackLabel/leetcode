#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []

        # Start digit from 1 to 8
        for i in range(1, 10):
            num = i
            # Next digit increases by 1
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    res.append(num)

        return sorted(res)
# @lc code=end

