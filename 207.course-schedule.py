#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

from enum import Enum
from typing import List


class State(Enum):
  kInit = 0
  kVisiting = 1
  kVisited = 2



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        states = [State.kInit] * numCourses

        for v, u in prerequisites:
            graph[u].append(v)

        def hasCycle(u: int) -> bool:
            if states[u] == State.kVisiting:
                return True
            if states[u] == State.kVisited:
                return False
            states[u] = State.kVisiting
            if any(hasCycle(v) for v in graph[u]):
                return True
            states[u] = State.kVisited
            return False

        return not any(hasCycle(i) for i in range(numCourses))
# @lc code=end

