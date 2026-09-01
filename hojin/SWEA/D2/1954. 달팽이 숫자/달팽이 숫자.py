T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    dx = [0, 1, 0, -1] # 우(0), 하(1), 좌(2), 상(3)
    dy = [1, 0, -1, 0]

    rotate_map = [[0] * N for _ in range(N)]

    cur_x, cur_y, cur_dirrection = 0, 0, 0  # (x, y, 현재 direction)

    for num in range(1, N * N + 1):
        rotate_map[cur_x][cur_y] = num

        new_x = cur_x + dx[cur_dirrection]
        new_y = cur_y + dy[cur_dirrection]

        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or rotate_map[new_x][new_y] != 0:
            cur_dirrection = (cur_dirrection + 1) % 4
            new_x = cur_x + dx[cur_dirrection]
            new_y = cur_y + dy[cur_dirrection]

        cur_x, cur_y = new_x, new_y

    print(f"#{test_case}")
    for i in range(N):
        print(*rotate_map[i])