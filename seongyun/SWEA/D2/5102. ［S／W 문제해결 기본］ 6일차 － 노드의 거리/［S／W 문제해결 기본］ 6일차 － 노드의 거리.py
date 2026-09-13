from collections import deque

def solve():
    v, e = map(int, input().split())
    edge = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
        
    s, g = map(int, input().split())

    q = deque([(s, 0)])
    visited = [False] * (v + 1)
    visited[s] = True

    while q:
        cur, dist = q.popleft()

        for node in edge[cur]:
            if node == g:
                return dist + 1
            
            if not visited[node]:
                q.append((node, dist + 1))
                visited[node] = True

    return 0

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")