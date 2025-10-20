#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        n = len(img1)
        max_overlaps = 0

        def count_overlaps(x_shift: int, y_shift: int) -> int:
            overlaps = 0
            for r in range(n):
                for c in range(n):
                    if 0 <= r + y_shift < n and 0 <= c + x_shift < n:
                        overlaps += img1[r][c] & img2[r + y_shift][c + x_shift]
            return overlaps

        for x_shift in range(-n + 1, n):
            for y_shift in range(-n + 1, n):
                max_overlaps = max(max_overlaps, count_overlaps(x_shift, y_shift))

        return max_overlaps
# @lc code=end

