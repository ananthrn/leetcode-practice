from sortedcontainers import SortedList
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(SortedList)
        self.userFollows = defaultdict(set)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.timestamp += 1
        self.userTweets[userId].add((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = SortedList()
        
        print("userId: ", userId)
        print("following: ", self.userFollows[userId])
        
        # allUsers = self.userFollows[userId]
        for followUserId in self.userFollows[userId].union({userId}):
            thisTweets = self.userTweets[followUserId][-10:]
            
            tweets.update(thisTweets)
            
            # print("thisTweets: ", thisTweets)
            
            if len(tweets) > 10:
                del tweets[0:len(tweets) - 10]
        
        
        tweetIds = [tweet[1] for tweet in tweets[-10:]]
        print("tweets: ", tweets)
        print("tweetIds: ", tweetIds)
        print()
        return tweetIds[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)