class Twitter {
private:
    // {user, time, post}
    // user -> {user, user, user, user}
    std::priority_queue<std::tuple<int, int, int>> feed; 
    std::unordered_map<int, std::unordered_set<int>> follow_list;
    int time = 0;
public:
    Twitter() {}
    
    void postTweet(int userId, int tweetId) {
        feed.push({time, userId, tweetId});
        time++;
    }
    

    vector<int> getNewsFeed(int userId) {
        auto copy_feed = feed;
        std::vector<int> res;
        while(!copy_feed.empty() && res.size() < 10){
            auto [t, u_id, tweet] = copy_feed.top();
            if (userId == u_id || follow_list[userId].contains(u_id)){
                res.push_back(tweet);
            }
            copy_feed.pop();
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        follow_list[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        follow_list[followerId].erase(followeeId);
    }
};
