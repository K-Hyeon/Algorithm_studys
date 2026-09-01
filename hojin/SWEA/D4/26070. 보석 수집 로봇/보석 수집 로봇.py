from collections import deque
T = int(input())
def bfs(N, matrix,treasure_num, start_dir, start_r, start_c):
    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 회전 횟수

    answer = tuple()
    queue = deque([(start_r,start_c, start_dir, 0)])
    while queue:
        r, c, dir, rot_cnt = queue.popleft()

        if matrix[r][c] == treasure_num:

            return r, c, dir, rot_cnt

        #직진한뒤에
        nr, nc = r + dr[dir], c + dc[dir]
        if 0 <=nr<N and 0<=nc<N:
            #보석이면 무조건 안돌기
            if matrix[nr][nc] == treasure_num:
                queue.append((nr, nc, dir, rot_cnt))
            else:
                # 안돌기
                queue.append((nr, nc, dir, rot_cnt))
                #돌기
                rot_dir = (dir+1) % 4
                queue.append((nr,nc, rot_dir, rot_cnt+1))





for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    treasure_list = []
    #보석 좌표를 계산
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                treasure_list.append(matrix[i][j])
    treasure_list.sort()

    #시작 위치
    start_r = 0
    start_c = 0

    #현재 위치
    current_r = start_r
    current_c = start_c

    #현재 방향
    current_dir = 0

    for treasure_num in treasure_list:
        #r, c, dir, rot_cnt =
        r, c, dir, rot_cnt = bfs(N,matrix,treasure_num, current_dir,current_r, current_c)
        #print(r,c,dir,rot_cnt)
        current_r = r
        current_c = c
        current_dir = dir
        result += rot_cnt

    print(f'#{test_case} {result}')