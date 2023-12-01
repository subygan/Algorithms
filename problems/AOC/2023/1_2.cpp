#include <string>
#include <vector>
#include <fstream>
using namespace std;


int checkWord(std::string line) {

    vector<string> v{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
//    printf("%s\n", line.c_str());
    for (int i = 0; i<v.size(); i++) {
//        printf("%s\n", v[i].c_str());
        if (line.starts_with(v[i])) {
//            printf("!!!!!!");
            return i+1;
        }
    }
//    printf("!!!!\n");

    int c = line[0] - '0';
    if ( c > -1 && c < 10) {return c;}
    return -1;
}

int main() {
    std::ifstream input("./1.txt");
    std::string line;
    int total = 0;
    while (std::getline(input, line)) {
        int prev = -1;
        int first;
        for (int i = 0; i < line.size(); i++) {
            int n = checkWord(line.substr(i));
            if (n>0) {
                if (prev == -1){
//                    printf("first: %d\n", n);
                  first = n;
                }
                prev = n;
            }
        }
        printf("%d %d\n", first, prev);
        total += first*10 + prev;
    }
    printf("%d\n", total);
    input.close();
    return 0;
}

