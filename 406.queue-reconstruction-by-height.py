#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []
        for person in people:
            queue.insert(person[1], person)

        return queue
# @lc code=end

