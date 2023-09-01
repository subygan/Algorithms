#include <iostream>
#include <vector>

using namespace std;

vector<int> getRow(int rowIndex) {

    vector<int> prev;
    for (int i = 0; i <= rowIndex; i++) {
        vector<int> cur(i + 1, 1);

        for (int j = 1; j < i; j++) cur[j] = prev[j] + prev[j - 1];

        prev = cur;
    }
    return prev;
}

int main() {

}

//