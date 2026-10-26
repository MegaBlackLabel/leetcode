#
# @lc app=leetcode id=1311 lang=python3
#
# [1311] Get Watched Videos by Your Friends
#

# @lc code=start
from collections import Counter, deque


class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        queue = deque([id])
        visited = {id}
      
        for _ in range(level):
            current_level_size = len(queue)
            for _ in range(current_level_size):
                current_person = queue.popleft()
                for friend_id in friends[current_person]:
                    if friend_id not in visited:
                        visited.add(friend_id)
                        queue.append(friend_id)

      
        video_count = Counter()
        for person_id in queue:
            for video in watchedVideos[person_id]:
                video_count[video] += 1
      
        return sorted(video_count.keys(), key=lambda video: (video_count[video], video))
# @lc code=end

