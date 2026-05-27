#
# @lc app=leetcode id=3492 lang=python3
#
# [3492] Maximum Containers on a Ship
#

# @lc code=start
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        max_cells = n * n
        
        containers_by_weight = maxWeight // w
    
        return min(max_cells, containers_by_weight)
# @lc code=end

