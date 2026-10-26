struct Node{
    int key;
    int val;
    Node* next;
    // responsible for deleting
    Node* prev;
};

class LRUCache {
private:
    int capacity;
    std::unordered_map<int, Node*> values;
    Node head;
    Node tail;

    void removeNode(Node* node){
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void addToBack(Node* node){
        Node* last = tail.prev;

        last->next = node;
    
        node->prev = last;
        node->next = &tail;

        tail.prev = node;
    }
public:
    LRUCache(int capacity) 
    :capacity(capacity) {
        head.next = &tail;
        tail.prev = &head;
    }
    
    int get(int key) {
        auto it = values.find(key);
        if (it == values.end()){
            return -1;
        }
        removeNode(values.at(key));
        addToBack(values.at(key));
        
        return (it->second)->val;
    }
    
    void put(int key, int value) {
        // new key
        auto it = values.find(key);
        if(it == values.end()){
            Node* newNode = new Node();
            newNode->val = value;
            newNode->key = key;
            values[key] = newNode;
            addToBack(values.at(key));
        } else {
            Node* node = it->second;
            node->val = value;
            removeNode(node);
            addToBack(node);
        }
        
        // full cash
        if (values.size() > capacity){
            Node* lru = head.next;
            removeNode(lru);
            values.erase(lru->key);
            delete lru;
        }
    }
};
