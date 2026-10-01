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
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = head;
        ListNode* prev = nullptr;
        
        // null -> 1 -> 2 -> 3

        while (cur){
            // temp a pointer to cur->next;
            ListNode* temp = cur->next;
            // cur->next = pre
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        return prev;
    }
};
