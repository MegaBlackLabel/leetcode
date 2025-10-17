#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc code=start
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        total_profit = 0
        max_profit = 0
        job_index = 0

        for ability in worker:
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            total_profit += max_profit

        return total_profit
# @lc code=end

