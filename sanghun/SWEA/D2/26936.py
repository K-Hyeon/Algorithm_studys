from collections import deque

def BFS(S, G, V, A):
    visited = [-1] * (V + 1)

    queue = deque([S])
    visited[S] = 0  # 출발 역은 이동 구간 0

    while queue:
        now_Node = queue.popleft()

        # 목적지 G에 도달하면 최단 구간 수 반환
        if now_Node == G:
            return visited[now_Node]

        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)

    # 연결되어 있지 않아 갈 수 없는 경우
    return 0


# 테스트 케이스 입력
T = int(input())

for i in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접 리스트
    A = [[] for _ in range(V + 1)]

    # 양방향 선로 입력
    for _ in range(E):
        a, b = map(int, input().split())
        A[a].append(b)
        A[b].append(a)

    S, G = map(int, input().split())

    result = BFS(S, G, V, A)

    print(f"#{i} {result}")
