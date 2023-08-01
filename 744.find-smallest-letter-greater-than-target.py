#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = bisect.bisect_right(range(len(letters)), target,
                                key=lambda m: letters[m])
        return letters[length % len(letters)]
# @lc code=end

