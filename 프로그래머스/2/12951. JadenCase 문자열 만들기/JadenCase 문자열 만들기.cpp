#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s) {
    string answer = "";
    for(int i = 0 ; i < s.size() ; i++){
        //공백문자가 아니고
        if(!isspace(s[i])){
            //단어의 첫문자인지 확인
            if(i == 0 || isspace(s[i-1])){
                //해당 문자가 숫자가 아니면
                if(!isdigit(s[i])){
                    answer += toupper(s[i]);
                    continue;
                }
            }else{
                //첫문자가 아니면 대문자인지 확인해서 대문자이면 소문자로 붙인다.
                if(isupper(s[i])){
                    answer += tolower(s[i]);
                    continue;
                }
            }
        }
        answer += s[i];
    }
    return answer;
}