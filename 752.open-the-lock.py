#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1

        queue = [("0000", 0)]
        visited = {"0000"}

        while queue:
            node, step = queue.pop(0)
            if node == target:
                return step

            for i in range(4):
                digit = int(node[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_node = node[:i] + str(new_digit) + node[i + 1:]
                    if new_node not in dead_set and new_node not in visited:
                        visited.add(new_node)
                        queue.append((new_node, step + 1))

        return -1
# @lc code=end

