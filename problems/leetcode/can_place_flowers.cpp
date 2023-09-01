class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        for(int i = 0; i<flowerbed.size(); i++) {
            int prev = (i==0) ? 0: flowerbed[i-1];
            int cur = flowerbed[i];
            int next = (i==flowerbed.size()-1)? 0:flowerbed[i+1];
            if (prev == 1 || cur == 1 || next == 1) {
                prev = cur;
                continue;
            }
            flowerbed[i] = 1;
            prev = 1;
            count+=1;
        }
        if(count>=n){return true;}
        return false;

    }
};