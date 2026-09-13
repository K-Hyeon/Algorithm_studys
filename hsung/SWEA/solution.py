import sys 
sys.stdin = open("1949/sample_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r, c, length, used, current_h):
    global ans, N, K, grid, visited
    
    ans = max(ans, length)
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        # visited 확인
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            
            # case 1 : 높이 안깍아도 방문할 수 있는 경우 
            if grid[nr][nc] < current_h:
                visited[nr][nc] = True
                DFS(nr, nc, length + 1, used, grid[nr][nc]) 
                visited[nr][nc] = False  # 완탐
                
            # 2. case 2 : 높이 깍아야 하는 경우 k정도 깎으면 가능함?
            elif not used and grid[nr][nc] - K < current_h:
                visited[nr][nc] = True
                DFS(nr, nc, length + 1, True, current_h - 1) #딱 현재 위치 높이의 -1 까지 깍자. 
                visited[nr][nc] = False  


test_case = int(input())
for tc in range(1, test_case + 1): 
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    max_h = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] > max_h:
                max_h = grid[r][c]
            
    starts = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] == max_h:
                starts.append((r, c))
                
    ans = 0
    visited = [[False] * N for _ in range(N)] # 그리드 visited은 boolean으로 하는게 효율적임
    
    #시작 
    for sr, sc in starts:
        visited[sr][sc] = True
        DFS(sr, sc, 1, False, grid[sr][sc])
        visited[sr][sc] = False
        
    print(f"#{tc} {ans}")