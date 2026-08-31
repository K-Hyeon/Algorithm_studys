from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    dx = [0, 1, 0, -1] # 우(0), 하(1), 좌(2), 상(3)
    dy = [1, 0, -1, 0]

    rotate_map = [[0] * N for _ in range(N)]
    search_queue = deque()

    search_queue.append((0, 0, 0, 1)) # (x, y, 현재 direction, 현재 번호)
    while search_queue:
        cur_x, cur_y, cur_dirrection, cur_num = search_queue.popleft()
        rotate_map[cur_x][cur_y] = cur_num

        new_x = cur_x + dx[cur_dirrection]
        new_y = cur_y + dy[cur_dirrection]

        if 0 <= new_x < N and 0 <= new_y < N and rotate_map[new_x][new_y] == 0:
            search_queue.append((new_x, new_y, cur_dirrection, cur_num + 1))

        # new 방향이 map범위를 넘어가거나, 이미 값이 채워진 상태일 때, 
        elif cur_num != N*N: # 현재 숫자가 N*N과 같다면 map이 모두 채워진 상태이므로 continue 
            next_dirrection = (cur_dirrection + 1) % 4
            new_x = cur_x + dx[next_dirrection]
            new_y = cur_y + dy[next_dirrection]
            search_queue.append((new_x, new_y, next_dirrection, cur_num + 1))


    print(f"#{test_case}")
    for i in range(N):
        print(*rotate_map[i])
