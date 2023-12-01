#include <string>
#include <vector>
#include <fstream>


int main() {
    std::ifstream input("./1.txt");
    std::string line;
    std::vector<std::string> lines;
    int total = 0;
    while (std::getline(input, line)) {
        printf("%s\n", line.c_str());
        int prev = -1;
        int first;
        for (char &c: line) {
            int i = c - '0';
            if (i > -1 && i < 10) {
                if (prev == -1){
                  first = i;
                }
                prev = i;
            }
        }
        total += first*10 + prev;
    }
    printf("%d\n", total);
    input.close();
    return 0;
}

