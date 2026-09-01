from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    
    queue = deque([S])
    dis = [1e9] * (V+1)
    dis[S] = 0
    answer = 0
    while queue:
        temp = queue.popleft()
        if temp == G: answer = dis[temp]
        for next_value in graph[temp]:
            if dis[next_value] > (dis[temp]+1):
                dis[next_value] = dis[temp] + 1
                queue.append(next_value)
            else: continue
    print(f"#{test_case} {answer}")
