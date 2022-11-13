import heapq


class Twitter:

    def __init__(self):
        self.twitter = {}
        self.timestamp = 0
        # user: {follower: set(),  posts: []}

    def createUser(self, userId):
        self.twitter[userId] = {
            'tweets': [],
            'following': set([userId])
        }

    #     def createUserIfNotExist(self, userId):
    #         if userId not in self.twitter:
    #             self.twitter[userId] = {
    #                     'tweets': [],
    #                     'following': set([userId])
    #                 }

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.twitter:
            self.createUser(userId)
        self.twitter[userId]['tweets'].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.twitter:
            self.createUser(userId)
        # combine all last 10 tweets from each its following
        # use a heap, and pop first 10 of them
        heap = []
        for following in self.twitter[userId]['following']:  # O(len(following))
            followingTweets = self.twitter[following]['tweets']
            if len(followingTweets) < 10:
                heap += followingTweets
            else:
                heap += followingTweets[len(followingTweets) - 10:]
        heapq.heapify(heap)  # O(n)
        res = []
        while len(res) < 10 and heap:  # . O(1)
            res.append(heapq.heappop(heap)[1])  # O(logn)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.twitter:
            self.createUser(followeeId)
        if followerId not in self.twitter:
            self.createUser(followerId)
        self.twitter[followerId]['following'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.twitter:
            self.createUser(followeeId)
        if followerId not in self.twitter:
            self.createUser(followerId)
        if followeeId in self.twitter[followerId]['following']:
            self.twitter[followerId]['following'].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)