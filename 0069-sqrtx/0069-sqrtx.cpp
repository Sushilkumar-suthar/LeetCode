#include <cmath>
class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) {
            return 0;
        } 
        
        double guess = x;

        while (fabs(guess * guess - x) > 1e-4) {
            guess = (guess + x / guess) / 2;
        }
        return std::floor(guess);
    }
};