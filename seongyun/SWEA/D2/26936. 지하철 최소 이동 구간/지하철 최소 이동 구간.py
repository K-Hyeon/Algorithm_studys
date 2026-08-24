from collections import deque

def solve():
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        st, dest = map(int, input().split())
        adj[st].append(dest)
        adj[dest].append(st)
    s, g = map(int, input().split())
    
    distance = [-1] * (v + 1)
    q = deque([(s)])
    distance[s] = 0
    while q:
        cur = q.popleft()
        
        for dest in adj[cur]:
            if distance[dest] == -1:
                distance[dest] = distance[cur] + 1
                q.append(dest)
    
    return 0 if distance[g] == -1 else distance[g]
    

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")