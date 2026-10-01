class Solution {
private:
    unordered_set<std::string> ops = {"+", "-", "*", "/"};

    int calculate(int a, int b, std::string s){
        if (s == "+"){
            return a + b;
        } else if (s == "-"){
            return b - a;
        } else if (s == "*"){
            return a * b;
        } else {
            return int(b / a);
        }
    }
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stack;
        for (std::string i : tokens){
            if (ops.contains(i)){
                int a = stack.top();
                stack.pop();
                int b = stack.top();
                stack.pop();
                int val = calculate(a, b, i);
                stack.push(val);
            } else {
                stack.push(stoi(i));
            }
        }
        return stack.top();
    }
};
