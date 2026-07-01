class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int l = 0;
        int s = 0;
        for(int i=0;i<nums.size();i++){
            s = s+nums[i];
        }
        for(int i=0;i<nums.size();i++){
            int r = s- nums[i]-l;
            if (l==r)
                return i;
            l = l+nums[i];
        }
        return -1;
    }
};