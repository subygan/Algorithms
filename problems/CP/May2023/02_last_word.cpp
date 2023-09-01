#include <iostream>

using namespace std;

int lengthOflastWord(string s){

    // trim trailing spaces
    size_t endpos = s.find_last_not_of(" \t");
    size_t startpos = s.find_first_not_of(" \t");
    if( std::string::npos != endpos )
    {
        s = s.substr( 0, endpos+1 );
        s = s.substr( startpos );
    }
    else {
        s.erase(std::remove(std::begin(s), std::end(s), ' '), std::end(s));
    }

    int count = 0;
    for (int i = s.length()-1; i>-1; i--){
        if (isspace(s[i])){
            return count;
        }
        count++;
    }
    return count;
}

int main(){
    cout << lengthOflastWord("Ssome some");
}


// https://leetcode.com/problems/length-of-last-word/
// #easy