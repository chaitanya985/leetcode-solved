class Twitter:

    def __init__(self):
        
        self.tweets = defaultdict(deque)
        
        self.following = defaultdict(set)
        
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.time += 1
        
        self.tweets[userId].appendleft((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        
        news_feed = []
        
        users = self.following[userId] | {userId}
        
        for user in users:
        
            news_feed.extend(self.tweets[user])
        
        return [tweetId for _, tweetId in sorted(news_feed, reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.following[followerId]:
        
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)