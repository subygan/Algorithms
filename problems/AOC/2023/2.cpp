#include <string>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;


//vector<string> splitUp(string s, string p) {
//    vector<string> res;
//    while (s.size() > 0) {
//        printf("%s\n", s.c_str());
//        string t = s.substr(0, s.find(p));
//        printf("!%s#!!!\n", t.c_str());
//        printf("!%s#!!!\n", t == " " ? "true" : "false");
//        if (t == " ") {
//            break;
//        }
//        res.push_back(t);
//        s.erase(0, s.find(p) + 1);
//    }
//    return res;
//}
//
//int main() {
//    std::ifstream input("./2.txt");
//    std::string line;
//    std::vector<std::string> lines;
//
//    int total = 0;
//    while (std::getline(input, line)) {
//        line.append(";");
//        int gameNumber = 0;
//        vector<string> semicolons = splitUp(line, ";");
////        break;
//        int i = 0;
//        bool valid = true;
//        while (i++ < semicolons.size()) {
//            printf("!!!!!\n");
//            string s = semicolons[i];
//            if (i == 0) {
//                auto g1 = splitUp(s, ":"); // "Game 1","1 red, 5 blue, 1 green"
//                gameNumber = stoi(splitUp(g1[1], " ")[1]); // "Game","1"
//                s.erase(0, s.find(":") + 1);
//            }
//            auto colors = splitUp(s+",", ",");
//            for (int j = 0; j < colors.size(); ++j) {
//                auto color = splitUp(colors[j], " ");
//                if ((color[1] == "red" && stoi(color[0]) > 12) || (color[1] == "blue" && stoi(color[0]) > 14) ||
//                    (color[1] == "green" && stoi(color[0]) > 13)) {
//                    valid = false;
//                    break;
//                }
//            }
//            if (!valid) { break; }
//        }
//        if (valid) { total += gameNumber; }
//    }
//    printf("%d\n", total);
//    input.close();
//    return 0;
//
//}


int main() {
    std::ifstream input("./2.txt");
    std::string line;
    std::vector<std::string> lines;

    int total = 0;
    while (std::getline(input, line)) {

        regex_search(line.front(), line.back(), regex("Game (\\d+)"));


    }


}