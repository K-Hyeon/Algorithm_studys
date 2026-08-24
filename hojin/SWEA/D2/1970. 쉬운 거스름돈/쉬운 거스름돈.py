T = int(input())
for test_case in range(1,T+1):
    money = [0,50000, 10000, 5000, 1000, 500, 100, 50, 10]

    n = int(input())
    dp = [0]*(len(money)+1)
    for i in range(1,len(money)):
        dp[i] = max(dp[i-1],dp[i-1]+ n//money[i])
        n -= (dp[i]-dp[i-1]) * money[i]

    #누적합 되돌리기
    result = []
    for i in range(1,len(dp)-1):
        result.append(dp[i] - dp[i-1])
    print(f'#{test_case}')
    [print(f'{item} ', end="") for item in result]
    print()