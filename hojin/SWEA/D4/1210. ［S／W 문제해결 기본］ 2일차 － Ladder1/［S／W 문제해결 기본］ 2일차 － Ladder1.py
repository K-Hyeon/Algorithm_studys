T=10
for test_case in range(1,T+1):
    t = int(input())
    result = 0
    ladder = [list(map(int, input().split())) for _ in range(100)]
    #도착지의 열 인덱스
    end_point = ladder[99].index(2)
    curr_r, curr_c = 99, end_point
    #상 좌 우
    dr = [-1, 0, 0]
    dc = [0, -1, 1]

    direction = 0
    while curr_r != 0:
        #왼쪽 벽에 붙었을때
        if curr_c == 0:
            #방향이 1인상태로 온거랑
            if direction == 1:
                direction = 0
            #방량이 0인상태로 온거
            elif direction == 0:
                #이때 오른 쪽을 검사
                right = curr_c + 1
                #1이면 방향을 튼다.
                if ladder[curr_r][right] == 1:
                    direction = 2
                else:
                    pass
        elif curr_c == 99:
            # 방향이 2인상태로 온거랑
            if direction == 2:
                direction = 0

            # 방량이 0인상태로 온거
            elif direction == 0:
                # 이때 왼 쪽을 검사
                left = curr_c - 1
                # 1이면 방향을 튼다.
                if ladder[curr_r][left] == 1:
                    direction = 1
                else:
                    pass
        else:
            right = curr_c + 1
            left = curr_c - 1
            #둘이 동시에 1이면 가로로 진행중이라는 뜻이므로 그대로 pass
            if ladder[curr_r][left] == 1 and ladder[curr_r][right] == 1:
                pass
            #왼쪽이 1이고 오른쪽이 1이 아닐때는 오른쪽으로 진행해왔거나 위로 진행해왔을때
            elif ladder[curr_r][left] == 1 and ladder[curr_r][right] != 1:
                #위로 진행해왔으면 왼쪽으로
                if direction == 0:
                    direction = 1
                #오른쪽이면 위로
                elif direction == 2:
                    direction = 0
            #오른쪽만 1이면 왼쪽으로 진행해왔거나 위로 진행해왔을때
            elif ladder[curr_r][left] != 1 and ladder[curr_r][right] == 1:
                # 위로 진행해왔으면 오른쪽으로
                if direction == 0:
                    direction = 2
                elif direction == 1:
                    direction = 0
            #다 아니면 둘다 0인거라 그냥 위로
            else:
                direction = 0


        curr_r += dr[direction]
        curr_c += dc[direction]
    result = curr_c
    print(f'#{test_case} {result}')