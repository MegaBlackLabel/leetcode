#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                ones = 0
                count = 0
                for y in range(max(0, i - 1), min(m, i + 2)):
                    for x in range(max(0, j - 1), min(n, j + 2)):
                        ones += img[y][x]
                        count += 1
                    ans[i][j] = ones // count

        return ans
# @lc code=end

