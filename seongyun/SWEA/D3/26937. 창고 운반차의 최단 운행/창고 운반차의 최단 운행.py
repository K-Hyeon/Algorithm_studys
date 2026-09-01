from collections import deque

def solve():
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                st = (r, c)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([st])
    board[st[0]][st[1]] = 1
    cnt = 0
    while q:
        repeat = len(q)
        
        for _ in range(repeat):
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
                    if board[nx][ny] == 3:
                        return cnt
                    q.append((nx, ny))
                    board[nx][ny] = 1
        cnt += 1
                
    return 0
    

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")