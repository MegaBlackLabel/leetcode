#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups_by_size = defaultdict(list)
      
        for person_index, required_group_size in enumerate(groupSizes):
            groups_by_size[required_group_size].append(person_index)
      
        result = []
        for group_size, people_indices in groups_by_size.items():
            for start_index in range(0, len(people_indices), group_size):
                group = people_indices[start_index:start_index + group_size]
                result.append(group)
      
        return result
# @lc code=end

