
from collections import deque


def BFS(start, A):
    # 정점 번호가 0~99까지이므로 크기 100으로 고정
    visited = [False] * 100
    queue = deque([start])
    visited[start] = True

    while queue:
        now_node = queue.popleft()

        # 목표점 99에 도달하면 성공
        if now_node == 99:
            return 1

        for next_node in A[now_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return 0


for tc in range(1, 11):
    test, n = map(int, input().split())

    # 전체 노드 번호는 0~99이므로 인접 리스트 크기를 100으로 고정
    A = [[] for _ in range(100)]

    edges = list(map(int, input().split()))

    # 입력 간선 정보 저장
    for i in range(0, len(edges), 2):
        u, v = edges[i], edges[i + 1]
        A[u].append(v)

    result = BFS(0, A)

    print(f"#{tc} {result}")
