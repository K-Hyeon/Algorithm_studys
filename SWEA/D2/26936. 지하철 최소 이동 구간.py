from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())

    distance = [-1] * (V + 1)
    distance[S] = 0
    queue = deque([S])

    while queue:
        cur = queue.popleft()
        if cur == G: break
        for next in graph[cur]:
            if distance[next] == -1:
                distance[next] = distance[cur] + 1
                queue.append(next)

    if distance[G] == -1: answer = 0
    else: answer = distance[G]

    print(f"#{test_case} {answer}")
