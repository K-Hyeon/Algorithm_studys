T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    max_fly = 0
    #십자
    cross_dr = [-1,1,0,0]
    cross_dc = [0,0,-1,1]

    diag_dr = [-1,-1,1,1]
    diag_dc = [-1,1,-1,1]

    for i in range(n):
        for j in range(n):
            #십자 형태로 뿌릴때
            #중심 포함
            fly_cnt = 0
            fly_cnt += grid[i][j]
            mul = 1
            while mul < m:
                for k in range(4):
                    nr = i + cross_dr[k] * mul
                    nc = j + cross_dc[k] * mul
                    if 0<=nr<n and 0<=nc<n:
                        fly_cnt += grid[nr][nc]
                mul += 1

            max_fly = max(max_fly, fly_cnt)
            #대각선으로 뿌릴때
            fly_cnt = 0
            fly_cnt += grid[i][j]
            mul = 1
            while mul < m:
                for k in range(4):
                    nr = i + diag_dr[k] * mul
                    nc = j + diag_dc[k] * mul
                    if 0 <= nr < n and 0 <= nc < n:
                        fly_cnt += grid[nr][nc]
                mul += 1
            max_fly = max(max_fly, fly_cnt)

    print(f"#{test_case} {max_fly}")