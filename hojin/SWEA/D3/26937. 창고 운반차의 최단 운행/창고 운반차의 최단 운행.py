from collections import deque
T = int(input())
def bfs(start_r,start_c,matrix,n):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]


    queue = deque([(start_r,start_c, 0)])
    visited = {(start_r,start_c)}
    while queue:
        r, c, length = queue.popleft()
        if matrix[r][c] == 3:
            return length - 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<n and 0<=nc<n and matrix[nr][nc] != 1 and (nr,nc) not in visited:
                visited.add((nr,nc))
                queue.append((nr,nc,length+1))

    return 0
for test_case in range(1,T+1):
    result = 0
    n = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                result = bfs(i,j,matrix,n)



    print(f'#{test_case} {result}')