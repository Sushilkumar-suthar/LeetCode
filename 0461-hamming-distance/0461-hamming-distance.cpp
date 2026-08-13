class Solution {
public:
    int hammingDistance(int x, int y) {
        int x2 = x ^ y;
        int setBits = 0;

        while (x2 > 0) {
            setBits += x2 & 1;
            x2 >>= 1;
        }

        return setBits;
    }
};