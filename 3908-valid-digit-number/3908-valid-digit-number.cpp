class Solution {
public:
    bool validDigit(int n, int x) {
        string s = to_string(n);

        return s[0] != ('0' + x) && s.find('0' + x) != string::npos;
    }
};