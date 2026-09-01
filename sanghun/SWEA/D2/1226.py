  
from collections import deque

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(start, graph):
    visited = [[False] * 16 for _ in range(16)]
    queue = deque([start])
    
    # 시작 위치 방문 처리
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 1. 먼저 범위 체크를 수행
            if 0 <= nx < 16 and 0 <= ny < 16:
                # 도착점에 도달한 경우
                if graph[nx][ny] == 3:
                    return 1
                
                # 벽이 아니고, 아직 방문하지 않은 경우
                if graph[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return 0


for _ in range(10):
    T = int(input())
    graph = [list(map(int, input().strip())) for _ in range(16)]

    start = None
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start = (i, j)
                break
        if start:
            break

    result = BFS(start, graph)
    print(f"#{T} {result}")
