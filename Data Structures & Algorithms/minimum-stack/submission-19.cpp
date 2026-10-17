class MinStack {
private:
    std::stack<int> s;
    std::stack<int> m_s;
public:
    MinStack() {}
    void push(int val) {
        s.push(val);
        if (m_s.empty()){ 
            m_s.push(val);
        } else {
            m_s.push(min(val, m_s.top()));
        }
    }
    
    void pop() {
        s.pop();
        m_s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return m_s.top();
    }
};
