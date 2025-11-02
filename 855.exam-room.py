#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#

# @lc code=start
from sortedcontainers import SortedList

class ExamRoom:

    def __init__(self, n: int):
        def calculate_distance(segment):
            left, right = segment
            if left == -1 or right == n:
                return right - left - 1
            else:
                return (right - left) >> 1
      
        self.n = n
        self.sorted_segments = SortedList(key=lambda segment: (-calculate_distance(segment), segment[0]))
      
        # Maps to track segment boundaries
        self.left_boundary = {}   # Maps right boundary -> left boundary
        self.right_boundary = {}  # Maps left boundary -> right boundary
      
        # Initially, the entire room is one empty segment from -1 to n
        self._add_segment((-1, n))

    def seat(self) -> int:
        best_segment = self.sorted_segments[0]
        position = (best_segment[0] + best_segment[1]) >> 1
      
        if best_segment[0] == -1:
            position = 0
        elif best_segment[1] == self.n:
            position = self.n - 1
      
        self._delete_segment(best_segment)
      
        self._add_segment((best_segment[0], position))
        self._add_segment((position, best_segment[1]))
      
        return position

    def leave(self, p: int) -> None:
        left_neighbor = self.left_boundary[p]
        right_neighbor = self.right_boundary[p]
      
        self._delete_segment((left_neighbor, p))
        self._delete_segment((p, right_neighbor))
      
        self._add_segment((left_neighbor, right_neighbor))

    def _add_segment(self, segment):
        self.sorted_segments.add(segment)
        self.left_boundary[segment[1]] = segment[0]
        self.right_boundary[segment[0]] = segment[1]
  
    def _delete_segment(self, segment):
        self.sorted_segments.remove(segment)
        self.left_boundary.pop(segment[1])
        self.right_boundary.pop(segment[0])

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end

