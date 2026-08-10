T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    blocks = [
        [],
        [2, 3, 1, 0],
        [1, 3, 0, 2],
        [3, 2, 0, 1],
        [2, 0, 3, 1],
        [2, 3, 0, 1]
    ]
    zeros = []
    wormhole_tmp = [(-1, -1)] * 5
    wormhole = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                zeros.append((i, j))
            elif 6 <= board[i][j] <= 10:
                idx = board[i][j] - 6
                if wormhole_tmp[idx] == (-1, -1):
                    wormhole_tmp[idx] = (i, j)
                else:
                    wormhole[(i, j)] = wormhole_tmp[idx]
                    wormhole[wormhole_tmp[idx]] = (i, j)

    ans = 0
    for (i, j) in zeros:
        st_point = (i, j)
        for d in range(4):
            score = 0
            x, y = i, j

            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    n = board[nx][ny]
                    if n == -1:
                        break
                    elif 6 <= n <= 10:
                        nx, ny = wormhole[(nx, ny)]
                    elif 1 <= n <= 5:
                        d = blocks[n][d]
                        score += 1
                    x, y = nx, ny

                else:
                    d = blocks[5][d]
                    x -= dx[d]
                    y -= dy[d]
                    score += 1

                if (x, y) == st_point:
                    break
            ans = max(score, ans)
    print(f"#{test_case} {ans}")