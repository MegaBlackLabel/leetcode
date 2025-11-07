#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
       

        graph = defaultdict(list)

        def build_graph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build_graph(node.right)

        build_graph(root)

        result = []
        visited = set()
        queue = deque([(target.val, 0)])
        visited.add(target.val)

        while queue:
            current_node, distance = queue.popleft()
            if distance == k:
                result.append(current_node)
            elif distance < k:
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))

        return result
# @lc code=end

