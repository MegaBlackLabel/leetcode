#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [height for _, height in
            sorted([(height, name) for name, height in zip(names, heights)], reverse=True)]
# @lc code=end

