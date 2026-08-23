
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(start, graph):
  queue = deque([start])
  visited = [[False] * 100 for _ in range(100)]
  visited[start[0]][start[1]] = True

  while queue:
    x, y  = queue.popleft()
    
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if 0<= nx < 100 and 0<= ny <100:

        if graph[nx][ny] == 3:
          return 1
        
        if graph[nx][ny] != 1 and not visited[nx][ny]:
          visited[nx][ny] = True
          queue.append((nx, ny))

  return 0


for _ in range(10):
  T = int(input())

  # 좌표를 입력 받는다
  graph = [list(map(int, input().strip())) for _ in range(100)]

  for i in range(100):
    for j in range(100):
      if graph[i][j] == 2:
        start = (i, j)

  result = BFS(start, graph)
  print(f"#{T} {result}")
