from collections import deque

def solve():
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    st = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == '*':
                continue
            cnt = 0
            for i in range(8):
                x, y = r + dx[i], c + dy[i]
                if 0 <= x < N and 0 <= y < N:
                    if board[x][y] == '*':
                        cnt += 1
            if cnt == 0:
                board[r][c] = 0
                st.append((r, c))
    
    ans = 0
    for point in st:
        if board[point[0]][point[1]] != 0:
            continue
        ans += 1
        board[point[0]][point[1]] = '*'

        q = deque([point])
        while q:
            x, y = q.popleft()
            
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != '*':
                    if board[nx][ny] == 0:
                        q.append((nx, ny))
                    board[nx][ny] = '*'
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                ans += 1
    return ans
    

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")