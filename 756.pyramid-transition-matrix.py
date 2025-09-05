#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#

# @lc code=start
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        allowed_map = {}
        for a in allowed:
            if a[:2] not in allowed_map:
                allowed_map[a[:2]] = []
            allowed_map[a[:2]].append(a[2])

        def backtrack(current: str) -> bool:
            if len(current) == 1:
                return True

            next_level = []
            for i in range(len(current) - 1):
                pair = current[i:i + 2]
                if pair not in allowed_map:
                    return False
                next_level.append(allowed_map[pair])

            def dfs(index: int, path: str) -> bool:
                if index == len(next_level):
                    return backtrack(path)
                for char in next_level[index]:
                    if dfs(index + 1, path + char):
                        return True
                return False

            return dfs(0, "")

        return backtrack(bottom)
# @lc code=end

