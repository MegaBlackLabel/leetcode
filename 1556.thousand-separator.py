#
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f'{n:,}'.replace(',', '.')
# @lc code=end

