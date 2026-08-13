T = int(input())
for test_case in range(1, T+1):
    #우하좌상
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    dir = 0
    r,c =0,0
    print(f"#{test_case}")
    for num in range(1,n*n+1):
        arr[r][c] = num
        nr, nc = r + dr[dir], c + dc[dir]
        if 0<=nr<n and 0<=nc<n and arr[nr][nc] == 0:
            r,c = nr,nc
        else:
            dir = (dir+1) % 4
            r,c = r + dr[dir], c + dc[dir]

    for row in arr:
        [print(item, end=" ") for item in row]
        print()