import heapq
from collections import defaultdict
from heapq import heappush, heappop


class Twitter2:
    def __init__(self):
        self.twitter = defaultdict(lambda: {"following": set(), "tweets": []})
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitter[userId]["tweets"].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) :
        # put most recent 1 post onto a heap for all followee
        # the top of the heap is the most recent, lets say it is posted by User 1
        # then the candidate of second recent must from rest of the heap,
        # and the second most recent of User 1
        # sort like have pointer on all of the followee, move the pointer once it points to the most recent

        # [time, tweetId, followeeId, followee_nth_recent_post]
        user = self.twitter[userId]
        heap = []
        if user["tweets"]:
            heappush(heap, [user["tweets"][-1][0], user["tweets"][-1][1], userId, 1])

        for followeeId in user["following"]:
            followee = self.twitter[followeeId]
            if followee["tweets"]:
                heappush(heap, [followee["tweets"][-1][0], followee["tweets"][-1][1], followeeId, 1])

        news_feed = []
        while len(news_feed) < 10 and heap:
            time, tweetId, followeeId, followee_nth = heappop(heap)
            news_feed.append(tweetId)

            if followee_nth == len(self.twitter[followeeId]["tweets"]):
                continue
            followee_nth += 1
            followee_nth_recent_tweet = self.twitter[followeeId]["tweets"][-1 * followee_nth]
            heappush(heap, [followee_nth_recent_tweet[0], followee_nth_recent_tweet[1], followeeId, followee_nth])

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.twitter[followerId]["following"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.twitter[followerId]["following"]:
            self.twitter[followerId]["following"].remove(followeeId)




class Twitter1:

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