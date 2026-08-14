from collections import deque

def solve():
    v, e = map(int, input().split())
    tmp = list(map(int, input().split()))
    graph = [[] for _ in range(v + 1)]
    indegree = [0] * (v + 1)

    for i in range(0, 2 * e, 2):
        graph[tmp[i]].append(tmp[i + 1])
        indegree[tmp[i + 1]] += 1

    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    ans = []
    while q:
        cur_v = q.popleft()
        ans.append(cur_v)

        for nxt in graph[cur_v]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return " ".join(map(str, ans))
    

for test_case in range(1, 11):
    print(f"#{test_case} {solve()}")
