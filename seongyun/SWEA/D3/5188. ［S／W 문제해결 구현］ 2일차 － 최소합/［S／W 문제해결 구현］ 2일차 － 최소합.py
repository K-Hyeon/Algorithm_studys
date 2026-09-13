def solve():
    N = int(input())
    board = []
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * N for _ in range(N)]
    dp[0][0] = board[0][0]

    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + board[i][0]

    for j in range(1, N):
        dp[0][j] = dp[0][j - 1] + board[0][j]

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + board[i][j]
    
    return dp[N - 1][N - 1]

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")