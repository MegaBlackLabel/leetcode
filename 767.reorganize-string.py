#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        if max(count.values()) > (len(s) + 1) // 2:
            return ''

        ans = []
        maxHeap = [(-freq, c) for c, freq in count.items()]
        heapq.heapify(maxHeap)
        prevFreq = 0
        prevChar = '@'

        while maxHeap:
            freq, c = heapq.heappop(maxHeap)
            ans.append(c)

            if prevFreq < 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))
            prevFreq = freq + 1
            prevChar = c

        return ''.join(ans)

# @lc code=end

