T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]
opposite = [0,2,1,4,3]


for test_case in range(1, T + 1):
    n,m,k = map(int,input().split())
    microbes= [list(map(int,input().split())) for _ in range(k)]



    for _ in range(m):
        max_val_arr = [[0]*n for _ in range(n)]
        dir_arr = [[0]*n for _ in range(n)]
        total_arr = [[0]*n for _ in range(n)]
        new_microbes = []

        for idx,microbe in enumerate(microbes):
            y,x,size,d = microbe

            ny = y + dy[d]
            nx = x + dx[d]
            if ny == n-1 or ny == 0 or nx == 0 or nx == n-1:
                d = opposite[d]
                size = int(size/2)

            total_arr[ny][nx] += size
            if max_val_arr[ny][nx] < size:
                max_val_arr[ny][nx] = size
                dir_arr[ny][nx] = d

        new_microbes = []
        for i in range(n):
            for j in range(n):
                if total_arr[i][j] != 0:
                    new_microbes.append([i,j,total_arr[i][j],dir_arr[i][j]])

        microbes = new_microbes

    print(f"#{test_case} {sum(total_arr[y][x] for y in range(n) for x in range(n))}")