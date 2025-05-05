#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#

# @lc code=start
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                if i != j:
                    dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    if dist in d:
                        d[dist] += 1
                    else:
                        d[dist] = 1
            for k in d.values():
                count += k * (k - 1)
        return count
# @lc code=end

