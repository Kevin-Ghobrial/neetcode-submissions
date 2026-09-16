class MinStack {
private:
    stack<long> minstack;
    stack<long> stack;

public:
    MinStack() {}
    
    void push(int val) {
        stack.push(val);
        if (minstack.empty()) {
            minstack.push(val);
        }else{
            minstack.push(min(minstack.top(), (long)val));
        }
        
    }
    
    void pop() {
        stack.pop();
        minstack.pop();
    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return minstack.top();
    }
};
