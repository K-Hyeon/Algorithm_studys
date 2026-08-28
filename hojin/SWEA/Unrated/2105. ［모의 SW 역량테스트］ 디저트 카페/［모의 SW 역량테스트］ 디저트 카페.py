T = int(input())

result = -1
def dfs(n,target_r, target_c, start_r, start_c, matrix, direction,length,desert_cnt_list):
    #print("target",target_r, target_c,"start", start_r, start_c,"direction", direction,"length",length,desert_cnt_list)
    # 우하, 좌하, 좌상, 우상 순서를 고정시킨다.
    global result
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    #만약 타겟 좌표와 같아지면 종료한다

    if length > 0 and start_r == target_r and start_c == target_c:

        result = max(result,length)
        return
    # 현재 방향대로 가는거랑 방향 + 1하는거
    for i in range(2):
        direction += i
        if direction < 4:
            nr = start_r + dr[direction]
            nc = start_c + dc[direction]

            if 0<=nr<n and 0<=nc<n:
                #다음좌표가 중복되면 종료
                if (nr == target_r and nc == target_c) or (matrix[nr][nc] not in desert_cnt_list):
                    #값을 desert_cnt_list에 넣는다.
                    if nr == target_r and nc == target_c:
                        #목표에 도착한거면 아무값도 추가하지 않고 길이만 추가
                        dfs(n, target_r, target_c, nr, nc, matrix, direction, length + 1, desert_cnt_list)
                    else:
                        desert_cnt_list.append(matrix[nr][nc])
                        dfs(n,target_r,target_c,nr,nc,matrix,direction,length+1,desert_cnt_list)
                        desert_cnt_list.remove(matrix[nr][nc])



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = -1
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]


    for i in range(n):
        for j in range(n):
            desert_cnt_list = [matrix[i][j]]
            dfs(n,i, j, i, j, matrix, 0,0,desert_cnt_list)


    print(f'#{test_case} {result}')
