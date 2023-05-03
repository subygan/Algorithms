#include <iostream>
#include <vector>
using namespace std;

vector<int> plusOne(vector<int>& digits) {
    digits.back() = digits.back()+1;
    int carry = 0;

    for (int it = digits.size() ; it -->0;){

        int v = digits.at(it);
        int plus = v+carry;
        digits.at(it) = plus%10;
        carry = plus/10;
        if (carry == 0) {
            break;
        }
    }

    if (carry == 1) {
     digits.insert(digits.begin(), 1);
    }

    return digits;
}

int main(){
    vector<int> i = {9};

    for(int j : plusOne(i)) {
        std::cout << j << ' ';
    };


}