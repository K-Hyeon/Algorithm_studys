from collections import deque

def solve():
    _ = int(input())
    board = [list(map(int, input().strip())) for _ in range(16)]
    
    for r in range(16):
        for c in range(16):
            if board[r][c] == 2:
                st = (r, c)
                break
        else:
            continue
        break
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([st])
    board[st[0]][st[1]] = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and board[nx][ny] != 1:
                if board[nx][ny] == 3:
                    return 1
                board[nx][ny] = 1
                q.append((nx, ny))
    return 0
    

for t in range(1, 11):
    print(f"#{t} {solve()}")