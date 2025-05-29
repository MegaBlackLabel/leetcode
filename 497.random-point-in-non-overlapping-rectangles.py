#
# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#

# @lc code=start
import itertools
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = list(itertools.accumulate(
            [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]))

    def pick(self) -> List[int]:
        index = bisect_right(self.areas, random.randint(0, self.areas[-1] - 1))
        x1, y1, x2, y2 = self.rects[index]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

