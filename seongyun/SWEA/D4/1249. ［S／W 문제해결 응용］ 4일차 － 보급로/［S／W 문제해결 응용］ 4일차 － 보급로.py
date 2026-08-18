import heapq

def solve():
    N = int(input())
    map_info = [list(map(int, input().strip())) for _ in range(N)]
    INF = 1e8

    visited = [[False for _ in range(N)] for _ in range(N)]
    dist = [[INF for _ in range(N)] for _ in range(N)]
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    q = []
    heapq.heappush(q, (0, 0, 0))
    dist[0][0] = 0

    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if d + map_info[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = d + map_info[nx][ny]
                    heapq.heappush(q, (d + map_info[nx][ny], nx, ny))

    return dist[N - 1][N - 1] 
    

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")
