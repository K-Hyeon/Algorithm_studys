#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(int argc, char** argv)
{
	int n;
    cin >> n;
    for(int i = 1 ; i <= n ; i++ ){
        string s = to_string(i);
        string answer = "";
        for(const char c : s){
            if(c == '3' || c == '6' || c == '9'){
                answer += "-";
            }
        }
        if(answer == ""){
            answer = s;
        }
        cout << answer << " ";
    }
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
