#include <iostream>
#include <vector>

using namespace std;

int main() {
    // 입출력 속도 향상 (알고리즘 문제 풀이 필수)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        int k;
        cin >> k;

        vector<int> st; // 파이썬의 stack 역할을 할 vector
        for (int i = 0; i < k; ++i) {
            int n;
            cin >> n;
            if (n == 0) {
                st.pop_back(); // 가장 최근에 넣은 값 제거
            } else {
                st.push_back(n); // 값 추가
            }
        }

        // 스택에 남아있는 값들의 합 구하기
        long long result = 0; // 합이 자릿수를 넘길 수 있으므로 long long 권장
        for (int num : st) {
            result += num;
        }

        cout << "#" << test_case << " " << result << "\n";
    }

    return 0;
}