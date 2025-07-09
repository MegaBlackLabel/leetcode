#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n == 0:
            return len(tasks)

        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1

        max_count = max(task_counts)
        max_count_tasks = task_counts.count(max_count)

        return max((max_count - 1) * (n + 1) + max_count_tasks, len(tasks))

# @lc code=end

