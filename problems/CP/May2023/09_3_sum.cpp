#include <iostream>
#include <vector>

using namespace std;

vector< vector<int> > threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
//    for (auto z: nums)std::cout << z << ' ';
    vector< vector<int> > res;
    for (int i=0;i<nums.size()-2;i++){
//        cout<<i<<endl;
        if (i > 0 && nums[i] == nums[i-1]) {
            continue;
        }
        for (int j = i; j<nums.size()-1;j++){
            int k = nums.size()-1;
            while (j<k){
//                cout<<i<<" "<<j<<" "<<k<<endl;
                if (nums[i] + nums[j] + nums[k] == 0) {
                    vector<int>v;
                    v.push_back(nums[i]);
                    v.push_back(nums[j]);
                    v.push_back(nums[k]);
                    res.push_back(v);
                while (j<k && nums[j]==nums[j+1]) j++;
                while (k>j && nums[k]==nums[k-1]) k--;
                }
                k--;
            }
        }
    }
    return res;
}

int main() {

    vector<int> v;
    v.push_back(0);
    v.push_back(3);
    v.push_back(-3);
    v.push_back(-3);
//    v.push_back(-4);
//    v.push_back(0);

//    for (auto j: v)std::cout << j << ' '<<endl;
    auto res = threeSum(v);
    for (auto i: res) {
        for (auto j: i)std::cout << j << ' ';
       cout << endl;
    }
}

// https://leetcode.com/problems/3sum/
// medium