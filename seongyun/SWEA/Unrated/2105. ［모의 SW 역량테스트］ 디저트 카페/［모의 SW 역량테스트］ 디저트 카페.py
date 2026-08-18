def solve():
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    dx = (1, 1, -1 ,-1)
    dy = (-1, 1, 1, -1)

    ans = -1
    for i in range(N):
        for j in range(N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if i + d1 + d2 >= N:
                        continue
                    if j - d1 < 0 or j + d2 >= N:
                        continue

                    visited = set()
                    cur_x, cur_y = i, j
                    possible = True

                    move_lengths = (d1, d2, d1, d2)
                    for idx in range(4):
                        length = move_lengths[idx]
                        for _ in range(length):
                            cur_x += dx[idx]
                            cur_y += dy[idx]

                            if cafes[cur_x][cur_y] in visited:
                                possible = False
                                break
                            visited.add (cafes[cur_x][cur_y])

                        if not possible:
                            break

                    if possible:
                        ans = max(ans, len(visited))

    return  ans

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")
