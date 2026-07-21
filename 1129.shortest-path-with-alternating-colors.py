#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [defaultdict(list), defaultdict(list)]
        for src, dst in redEdges:
            graph[0][src].append(dst)
        for src, dst in blueEdges:
            graph[1][src].append(dst)
            
        ans = [-1] * n
        
        visited = set()
        

        queue = deque([
            (0, 0, 0),
            (0, 0, 1)
        ])
        
        while queue:
            node, dist, next_color = queue.popleft()
            

            if ans[node] == -1:
                ans[node] = dist
                

            for neighbor in graph[next_color][node]:
                next_state = (neighbor, 1 - next_color)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((neighbor, dist + 1, 1 - next_color))
                    
        return ans
# @lc code=end

