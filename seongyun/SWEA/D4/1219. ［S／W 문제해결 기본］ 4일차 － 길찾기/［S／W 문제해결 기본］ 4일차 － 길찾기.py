from collections import defaultdict, deque

def solve():
    _, e = map(int, input().split())
    tmp = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(0, len(tmp), 2):
        u, v = tmp[i], tmp[i + 1]
        graph[u].append(v)
        
    visited = [False] * 100
    visited[0] = True
    q = deque([0])
    while q:
        cur = q.popleft()
        
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                if nxt == 99:
                    return 1
    return 0


for t in range(1, 11):
    print(f"#{t} {solve()}")