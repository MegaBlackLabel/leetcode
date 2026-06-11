#
# @lc app=leetcode id=1042 lang=python3
#
# [1042] Flower Planting With No Adjacent
#

# @lc code=start
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        result = [0] * n
        
        for i in range(n):
            neighbor_flowers = {result[neighbor] for neighbor in graph[i]}
            
            for flower in range(1, 5):
                if flower not in neighbor_flowers:
                    result[i] = flower
                    break
                    
        return result
# @lc code=end

