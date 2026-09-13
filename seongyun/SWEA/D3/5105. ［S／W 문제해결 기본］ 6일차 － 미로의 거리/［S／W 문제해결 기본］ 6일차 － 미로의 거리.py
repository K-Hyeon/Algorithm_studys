from collections import deque

def solve():
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]

    st, end = None, None
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                st = (i, j)
            elif board[i][j] == 3:
                end = (i, j)
    
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    q = deque([(st[0], st[1], 0)])
    board[st[0]][st[1]] = 1

    while q:
        cx, cy, dist = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (nx, ny) == end:
                return dist

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
                q.append((nx, ny, dist + 1))
                board[nx][ny] = 1
    
    return 0

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")