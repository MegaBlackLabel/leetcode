#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)
        return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])
# @lc code=end

