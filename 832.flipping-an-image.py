#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for item in image:
            inside = []
            for i in range(len(item)-1, -1, -1):
                inside.append(1 - item[i])
            ans.append(inside)
        return ans
# @lc code=end

