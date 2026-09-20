import sys
sys.stdin = open("5105/sample_input.txt", "r")

from collections import deque

def bfs(start_y, start_x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque([(start_y, start_x, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[start_y][start_x] = True

    while queue:
        y, x, dist = queue.popleft()
        if maze[y][x] == 3:
            return dist -1
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N:
                # 벽(0)이 아니고, 아직 방문하지 않은 길인지 확인
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, dist + 1))
    return 0             
                    
test_case = int(input())
for tc in range(test_case):
    N = int(input())
    
    maze = []
    for _ in range(N):
        maze.append(list(map(int, list(input()))))

    start_y, start_x = -1, -1 
    # end_y, end_x = -1, -1 #필요 없음 
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_y, start_x = i, j
            # if maze[i][j] == 3:
            #     end_y, end_x = i, j
            
    dist = bfs(start_y, start_x)
    print(f"#{tc + 1} {dist}")