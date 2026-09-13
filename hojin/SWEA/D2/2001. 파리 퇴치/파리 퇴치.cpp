#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin>>T;
	
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n,m;
        int current_max = 0;
		cin >> n >> m;
        vector<vector<int> > arr(n, vector<int>(n));
        for(int i = 0 ; i < n; i++){
            for(int j = 0 ; j < n; j++){
                cin >> arr[i][j];
            }
        }
        
        for(int i = 0 ; i < n-m+1 ; i++){
            for(int j = 0 ; j < n-m+1; j++){
                int sum = 0;
                for(int k = 0 ; k < m; k++){
                    for(int l = 0 ; l < m; l++){
                        sum += arr[i+k][j+l];
                    }
                }
                current_max = max(current_max, sum);
            }
        }
        cout << "#" << test_case << " " << current_max << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}