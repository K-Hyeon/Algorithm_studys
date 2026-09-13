import heapq

def solve():
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    INF = float('inf')
    dist = [[INF for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        cur_cost, cx, cy = heapq.heappop(pq)

        if cur_cost > dist[cx][cy]:
            continue

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                next_cost = cur_cost + board[nx][ny]

                if next_cost < dist[nx][ny]:
                    dist[nx][ny] = next_cost
                    heapq.heappush(pq, (next_cost, nx, ny))
    
    return dist[N - 1][N - 1]

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")