def dfs(x, y, len, isUsed):
    visited[x][y] = 1
    global ans
    ans = max(ans, len)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if maps[x][y] > maps[nx][ny]:
                dfs(nx, ny, len + 1, isUsed)
            elif not isUsed and maps[nx][ny] - K < maps[x][y]:
                tmp = maps[nx][ny]
                maps[nx][ny] = maps[x][y] - 1
                dfs(nx, ny, len + 1, True)
                maps[nx][ny] = tmp

    visited[x][y] = 0

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    max_height = max([max(row) for row in maps])
    max_height_pos = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_height:
                max_height_pos.append((i, j))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    ans = 0
    for i, j in max_height_pos:
        visited = [[0] * N for _ in range(N)]
        dfs(i, j, 1, False)

    print(f"#{test_case} {ans}")
