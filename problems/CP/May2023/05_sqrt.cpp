#include <iostream>

using namespace std;

int sqrt(int x){

    long long int mid;
    int low = 0;
    int high = x;
    if (x < 2) return x;
    while (low < high) {
        mid = (low + high) / 2;
        long long int sqr = mid * mid;
        if (sqr == x) return mid;
        if (sqr >  x) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    if (mid*mid > x) return mid - 1;

    return mid;
}

int main(){
    cout<<sqrt(0);
}

// https://leetcode.com/problems/sqrtx/description/
// easy