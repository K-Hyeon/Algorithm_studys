T = int(input())

def check(row, col):
    # 열 확인
    for i in range(row):
        if board[i][col] == 1:
            return False
    # 왼쪽 위 대각선 확인    
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
    # 오른쪽 위 대각선
    r = row - 1
    c = col + 1
    while r >= 0 and c < N:
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1
    return True

def dfs(row):
    global ans
    if row == N:
        ans += 1
        return
    # 현재 행의 모든 열을 확인
    for col in range(N):
        if check(row, col):
            board[row][col] = 1
            dfs(row + 1)
            board[row][col] = 0

for test_case in range(1, T + 1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    ans = 0
    dfs(0)
    print(f"#{test_case} {ans}")
