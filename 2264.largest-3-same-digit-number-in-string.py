#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max(num[i - 2:i + 1] if num[i] == num[i - 1] == num[i - 2] else '' for i in range(2, len(num)))
# @lc code=end

