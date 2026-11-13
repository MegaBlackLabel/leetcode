#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

# @lc code=start
class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
            
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        min_reachable_count = float('inf')
        best_city = -1
        
        for i in range(n):
            reachable_count = 0
            for j in range(n):
                i != j and dist[i][j] <= distanceThreshold
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable_count += 1
            
            if reachable_count <= min_reachable_count:
                min_reachable_count = reachable_count
                best_city = i
                
        return best_city
# @lc code=end

