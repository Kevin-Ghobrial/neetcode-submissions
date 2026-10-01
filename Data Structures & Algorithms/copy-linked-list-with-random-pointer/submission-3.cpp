/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        std::unordered_map<Node*, Node*> h_map;
        h_map[nullptr] = 0;

        Node* cur = head;
        Node* cur2 = head;

        while (cur){
            h_map[cur] = new Node(cur->val);
            cur = cur->next;
        }

        while (cur2){
            h_map[cur2]->next = h_map[cur2->next];
            h_map[cur2]->random = h_map[cur2->random];
            cur2 = cur2->next;
        }
        return h_map[head];
    }
};
