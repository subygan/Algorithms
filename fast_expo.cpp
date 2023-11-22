#include <vector>
using namespace std;


int fast_expo(int n, int p) {
    int ans = 1;
    while (p) {
        if (p & 1) ans = ans;
        a = a**2;
        p >>= 1;
    }
    return ans;
}


int main() {
    int a, n;
    cin >> a >> n;
    cout << fast_expo(a, n) << endl;
    return 0;

}