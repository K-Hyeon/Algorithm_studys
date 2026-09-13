#include <string>
#include <vector>
#include <bitset>
#include <iostream>
#include <algorithm>

using namespace std;
string to_binary(int n){
    if(n == 0) return "0";
    
    string res = "";
    while(n > 0){
        res += to_string(n%2);
        n /= 2;
    }
    reverse(res.begin(), res.end());
    return res;
}
vector<int> solution(string s) {
    vector<int> answer;
    int convert_cnt = 0;
    int zero_cnt = 0;
    
    while(s.size() > 1){
        for(char c : s){
            if(c == '0'){
                zero_cnt += 1;
            }
        }
        
        s.erase(remove(s.begin(), s.end(), '0'), s.end());
        int num = s.size();
        s = to_binary(num);
        convert_cnt += 1;
    }
    answer.push_back(convert_cnt);
    answer.push_back(zero_cnt);
    
    return answer;
}