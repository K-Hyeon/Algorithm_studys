from collections import deque

def solve():
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    max_home = 0
    for r in range(N):
        for c in range(N):
            visited = [[False for _ in range(N)] for _ in range(N)]
            q = deque([(r, c)])
            visited[r][c] = True

            k = 0
            cnt = 0

            while q:
                length = len(q)
                k += 1
                for _ in range(length):
                    cur_x, cur_y = q.popleft()
                    if town[cur_x][cur_y] == 1:
                        cnt += 1

                    for i in range(4):
                        nx, ny = cur_x + dx[i], cur_y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

                cost = k * k + (k - 1) * (k - 1)
                if cnt * M >= cost:
                    max_home = max(max_home, cnt)

    return max_home

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")
