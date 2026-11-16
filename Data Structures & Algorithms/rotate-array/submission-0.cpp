class Node {
public:
    Node* next;
    int val;

    Node(): val(0), next(nullptr){}
    Node(int val, Node* next): val(val), next(next){}
};


class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (n <= 1) return;
        
        k = k % n;
        if (k == 0) return;

        Node* dummy = new Node(0, nullptr);
        Node* cur = dummy;

        for (const auto& n : nums){
            cur->next = new Node(n, nullptr);
            cur = cur->next;
        }
        Node* head = dummy->next;
        cur->next = head;
        delete dummy;
        
        Node* cur2 = head;
        for (int i = 0; i < n - k; i++) {
            cur2 = cur2->next;
        }

        int j = 0;
        while(j < nums.size()){
            nums[j] = cur2->val;
            Node* temp = cur2;
            cur2 = cur2->next;
            delete temp;
            j++;
        }
    }
};