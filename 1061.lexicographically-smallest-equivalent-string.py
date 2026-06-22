#
# @lc app=leetcode id=1061 lang=python3
#
# [1061] Lexicographically Smallest Equivalent String
#

# @lc code=start
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x != root_y:
                if root_x < root_y:
                    parent[root_y] = root_x
                else:
                    parent[root_x] = root_y

        for c1, c2 in zip(s1, s2):
            union(c1, c2)
            
        res = [find(c) for c in baseStr]
        
        return "".join(res)
# @lc code=end

