#include <iostream>
#include <vector>

using namespace std;


vector<vector<int> > generate(int numRows) {

    vector<vector<int> > ans;

    for (int i = 0; i<numRows;i++){
        vector<int> row(i+1,1);
        for (int j = 1 ; j<i;j++ ) row[j] = ans[i-1][j]+ans[i-1][j-1];
        ans.push_back(row);
    }

    return ans;
}

int main(){

    for (auto i:generate(4)){
        for (auto j:i) cout<<j<<" ";
        cout<<endl;
    }

}

//