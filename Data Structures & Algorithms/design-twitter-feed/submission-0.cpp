class Twitter {
private:
    std::unordered_map<int, std::vector<int>> followList;
    std::priority_queue<std::tuple<int, int, int>> feed;
    int time {0};
public:
    Twitter() {}
    
    void postTweet(int userId, int tweetId) {
        feed.push({time, userId, tweetId});
        time++;
    }
    
    vector<int> getNewsFeed(int userId) {
        std::vector<int> res;
        auto pq_copy = feed;
        int counter {0};
        while (pq_copy.size() > 0 && counter < 10){
            auto [time, id, tweet] = pq_copy.top();
            auto follows = std::ranges::contains(followList[userId], id);
            if (id == userId || follows){
                res.push_back(tweet);
                counter++;
            }
            pq_copy.pop();
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        followList[followerId].push_back(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        auto& val = followList[followerId];
        std::erase_if(val, [&](int id){
            return id == followeeId;
        });
    }
};
