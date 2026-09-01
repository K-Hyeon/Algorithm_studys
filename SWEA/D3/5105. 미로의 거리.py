from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    for i in range(N):
        arr = list(map(int, input().strip()))
        for j in range(len(arr)):
            if arr[j] == 2: start = (i, j)
            elif arr[j] == 3: end = (i, j)
        graph.append(arr)
    
    # 0: 통로, 1: 벽, 2: 출발, 3:도착
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([start])
    dis = [[-1]*N for _ in range(N)]
    dis[start[0]][start[1]] = 0
    
    answer = 0
    while queue:
        temp = queue.popleft()
        if temp == end: answer= dis[temp[0]][temp[1]]-1
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 1 and dis[nx][ny] == -1:
                dis[nx][ny] = dis[temp[0]][temp[1]] + 1
                queue.append((nx, ny))
    print(f"#{test_case} {answer}")
