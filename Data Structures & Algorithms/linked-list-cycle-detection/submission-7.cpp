/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        std::set<ListNode*> visited;
        ListNode* cur = head;
        while (cur) {
            if (visited.contains(cur)){
                return true;
            }
            visited.insert(cur);
            cur = cur->next;
        }
        return false;
    }
};
