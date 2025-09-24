#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        order_index = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda c: order_index.get(c, len(order))))
# @lc code=end

