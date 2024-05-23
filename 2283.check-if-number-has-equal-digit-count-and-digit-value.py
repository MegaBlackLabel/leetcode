#
# @lc app=leetcode id=2283 lang=python3
#
# [2283] Check if Number Has Equal Digit Count and Digit Value
#

# @lc code=start
import collections


class Solution:
    def digitCount(self, num: str) -> bool:
        count = collections.Counter(num)
        return all(count[str(i)] == int(digit) for i, digit in enumerate(num))
# @lc code=end

