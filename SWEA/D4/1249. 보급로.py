from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    for _ in range(N):
        arr = list(map(int, input().strip()))
        graph.append(arr)
    
    dis = [[1e9]*N for _ in range(N)]
    dis[0][0] = 0
    queue = deque([(0, 0)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        temp = queue.popleft()
        if temp == (N-1, N-1): print(1)
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dis[temp[0]][temp[1]] + graph[nx][ny] < dis[nx][ny]:
                    dis[nx][ny] = dis[temp[0]][temp[1]] + graph[nx][ny]
                    queue.append([nx, ny])
    print(f"#{test_case} {dis[N-1][N-1]}")
