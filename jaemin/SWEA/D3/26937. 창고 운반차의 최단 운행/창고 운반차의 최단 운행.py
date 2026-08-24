from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    warehouse = [input() for _ in range(N)]

    # 시작점(2), 도착점(3) 찾기
    for r in range(N):
        for c in range(N):
            if warehouse[r][c] == '2':
                start = (r, c)
            elif warehouse[r][c] == '3':
                goal = (r, c)

    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # BFS
    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    answer = 0

    while queue:
        r, c, dist = queue.popleft()

        # 도착
        if (r, c) == goal:
            answer = dist - 1
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 창고 밖
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 이미 방문했거나 막힌 칸
            if visited[nr][nc] or warehouse[nr][nc] == '1':
                continue

            visited[nr][nc] = True
            queue.append((nr, nc, dist + 1))

    print(f'#{tc} {answer}')