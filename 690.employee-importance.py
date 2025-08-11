#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_map = {emp.id: emp for emp in employees}

        def dfs(emp_id):
            emp = emp_map[emp_id]
            total_importance = emp.importance
            for sub_id in emp.subordinates:
                total_importance += dfs(sub_id)
            return total_importance

        return dfs(id)
# @lc code=end

