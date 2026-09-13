from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발점
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start = (r, c)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[False] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]

    queue = deque([start])
    sr, sc = start
    visited[sr][sc] = True

    answer = 0

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 도착점
            if maze[nr][nc] == 3:
                answer = distance[r][c]
                queue.clear()
                break

            # 통로
            if maze[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))
        else:
            continue

        break

    print(f"#{tc} {answer}")