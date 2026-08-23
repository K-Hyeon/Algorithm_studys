from collections import deque
t = int(input())

def bfs(start, end, graph):

    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        curr, length = queue.popleft()
        if curr == end:
            return length

        for nxt in graph[curr]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt,length+1))

    return 0

for test_case in range(1,t+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        V1, V2 = map(int, input().split())
        graph[V1].append(V2)
        graph[V2].append(V1)
    S, G = map(int, input().split())

    result = bfs(S,G,graph)

    print(f'#{test_case} {result}')