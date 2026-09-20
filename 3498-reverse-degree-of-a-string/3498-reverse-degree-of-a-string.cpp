class Solution {
public:
    int reverseDegree(string s) {
        int sum = 0,i=0;
        char c=s[i];
        while(c!=NULL){
            sum+=(26-(c-96)+1)*(i+1);
            i+=1;
            c=s[i];
        }

        return sum;
    }
};