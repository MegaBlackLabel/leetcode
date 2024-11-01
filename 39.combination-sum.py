#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(cur,left,num):
            if left == 0:
                ans.append(cur+[])
                return
            for i in range(num,len(candidates)):
                if left-candidates[i] >= 0:
                    cur.append(candidates[i])
                    dfs(cur,left-candidates[i],i)
                    cur.pop()
        dfs([],target,0)
        return ans
# @lc code=end

