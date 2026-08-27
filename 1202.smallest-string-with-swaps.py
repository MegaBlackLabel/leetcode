#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        for a, b in pairs:
            union(a, b)
            
        from collections import defaultdict
        group = defaultdict(list)
        for i in range(len(s)):
            group[find(i)].append(i)
            
        res = list(s)
        for indices in group.values():
            chars = sorted([s[i] for i in indices])
            indices.sort()
            for i, c in zip(indices, chars):
                res[i] = c
                
        return "".join(res)
# @lc code=end

