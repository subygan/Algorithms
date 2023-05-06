#include <iostream>
#include <map>
#include <vector>

using namespace std;

int start(int n, vector<int> &v){

    if (n<=2) return n;
    if (v[n] != -1) return v[n] ;

    return v[n] =  start(n-1, v) + start(n-2, v);
}

int climb(int n) {
    vector<int> m(n+1);
    for (int i=1;i<=n; i++){
        m[i] = -1;
    }
    return start(n, m);
}


int main(){
    cout<<climb(45);
}

// https://leetcode.com/problems/climbing-stairs
// easy