#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#

# @lc code=start
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.times = times
        self.leaders = []
        count = {}
        leader = -1
        max_votes = 0

        for person in persons:
            count[person] = count.get(person, 0) + 1
            if count[person] >= max_votes:
                if person != leader:
                    leader = person
                max_votes = count[person]
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        
        left, right = 0, len(self.times) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.leaders[left]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

