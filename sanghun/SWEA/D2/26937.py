
from collections import deque
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(i, j, N, graph):
    queue = deque()
    queue.append((i, j))
    # 우선 -1로 넣어서 배정해준다 
    visited = [[-1] * N for _ in range(N)]

    # 처음 시작점을 0 으로 대입해준다 
    visited[i][j] = 0

    # 큐를 돌리면서 
    while queue:
        # 현재를 큐에서 제외해주고 
        now = queue.popleft()

        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]

            # 그 위치가 이제 정사각형 안에 있으면 
            if x >= 0 and y >= 0 and x < N and y < N:

                if graph[x][y] == 3:
                    return visited[now[0]][now[1]] 


                # 그리고 방문하지 않았고, 그래프에서도 막혀있지 않았고, 최종 지점이 아니라면 
                if visited[x][y] == -1 and graph[x][y] ==0:
                    # 방문한걸로 체크하며 1을 더해준다 
                    visited[x][y] = visited[now[0]][now[1]] + 1
                    queue.append((x, y)) 
                
    return 0 


for tc in range(1, T+1):
    N = int(input())
    
    # 좌표 부터 입력 받기 
    graph = [list(map(int, input().strip())) for _ in range(N)]


    # 2가 어디에 있는지 찾는다
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                start_x = i
                start_y = j
                break 


    result = BFS(start_x, start_y, N, graph)

    print(f"#{tc} {result}")
