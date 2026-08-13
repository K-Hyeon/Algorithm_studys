from collections import deque
import pprint

def solve():
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]

    max_home = 0
    for r in range(N):
        for c in range(N):
            cnt = 0
            if town[r][c] == 1:
                cnt += 1

            visited = [[False for _ in range(N)] for _ in range(N)]
            dx = (1, -1, 0, 0)
            dy = (0, 0, 1, -1)

            q = deque()
            q.append((r, c))
            visited[r][c] = True
            k = 1

            cost = cnt*M - (k*k + (k-1)*(k-1))
            if cost >= 0:
                max_home = max(max_home, cnt)
            while q:
                length = len(q)
                k += 1
                for _ in range(length):
                    cur_x, cur_y = q.popleft()
                    for i in range(4):
                        nx = cur_x + dx[i]
                        ny = cur_y + dy[i]

                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            visited[nx][ny] = True
                            if town[nx][ny] == 1:
                                cnt += 1
                            q.append((nx, ny))

                cost = cnt*M - (k*k + (k-1)*(k-1))
                if cost >= 0:
                    max_home = max(max_home, cnt)

    return max_home

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")
