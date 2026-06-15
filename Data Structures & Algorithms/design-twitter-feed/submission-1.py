from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 1
        self.users = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.count * -1, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        user_list = self.users[userId] | {userId}
        for follows in user_list:
            for posts in self.posts[follows]:
                heapq.heappush(heap, posts)

        res = []
        for i in range(10):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)