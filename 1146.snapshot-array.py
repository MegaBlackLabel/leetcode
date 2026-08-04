#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
from bisect import bisect_left
from typing import List, Tuple


class SnapshotArray:

    def __init__(self, length: int):
        self.array_history: List[List[Tuple[int, int]]] = [[] for _ in range(length)]
        self.current_snap_id: int = 0

    def set(self, index: int, val: int) -> None:
        self.array_history[index].append((self.current_snap_id, val))

    def snap(self) -> int:
        snapshot_id = self.current_snap_id
        self.current_snap_id += 1
        return snapshot_id

    def get(self, index: int, snap_id: int) -> int:
        history = self.array_history[index]
        insertion_point = bisect_left(history, (snap_id, inf)) - 1

        if insertion_point < 0:
            return 0

        return history[insertion_point][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

