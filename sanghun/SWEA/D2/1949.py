import sys

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, current_height, length, k_used):
    global max_length
    
    # 최장 길이를 지속적으로 갱신
    if length > max_length:
        max_length = length
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 지도 범위 체크 및 방문 여부 확인
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 1. 공사 없이 이동할 수 있는 경우 (다음 위치가 현재 높이보다 낮은 경우)
            if grid[nx][ny] < current_height:
                visited[nx][ny] = True
                dfs(nx, ny, grid[nx][ny], length + 1, k_used)
                visited[nx][ny] = False  # 백트래킹
                
            # 2. 아직 공사를 하지 않았고, 깎아서 이동할 수 있는 경우
            elif not k_used and grid[nx][ny] - K < current_height:
                visited[nx][ny] = True
                # 이동 가능하도록 현재 높이보다 딱 1만큼 작게 깎는 것이 가장 유리함
                dfs(nx, ny, current_height - 1, length + 1, True)
                visited[nx][ny] = False  # 백트래킹

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 가장 높은 봉우리 높이 찾기
    max_h = max(max(row) for row in grid)
    
    max_length = 0
    visited = [[False] * N for _ in range(N)]
    
    # 가장 높은 봉우리인 출발점 위치 탐색 및 DFS 실행
    for i in range(N):
        for j in range(N):
            if grid[i][j] == max_h:
                visited[i][j] = True
                dfs(i, j, max_h, 1, False)
                visited[i][j] = False  # 백트래킹
                
    print(f"#{tc} {max_length}")
