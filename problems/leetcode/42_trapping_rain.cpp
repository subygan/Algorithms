class Solution {
public:
    int trap(vector<int>& height) {
        int lmax = INT_MIN, rmax = INT_MIN, l = 0, r = height.size()-1, res = 0;

        while (l<r){
            lmax = max(lmax, height[l]);
            rmax = max(rmax, height[r]);
            res += lmax<rmax?lmax-height[l++]:rmax-height[r--];
        }
        return res;
    }
};