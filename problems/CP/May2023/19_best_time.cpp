#include <iostream>
#include <vector>

using namespace std;

int maxProfit(vector<int>& prices) {

    int minSoFar = INT_MAX, profit = 0;

    for (int i= 0; i <prices.size();i++) {
        minSoFar = min(minSoFar,prices[i]);
        profit = max(profit, prices[i]-minSoFar);
    }
    return profit;

}

int main(){

}


// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// easy