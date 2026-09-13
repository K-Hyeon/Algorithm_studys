from collections import deque

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접 리스트
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())

        # 방향이 없는 그래프이므로 양쪽 모두 연결
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())

    # 방문 여부 + S에서 해당 노드까지의 거리
    distance = [0] * (V + 1)

    queue = deque([S])

    # 시작 노드는 방문 처리
    distance[S] = 1

    while queue:
        current = queue.popleft()

        # 목적지에 도착
        if current == G:
            break

        for next_node in graph[current]:
            if distance[next_node] == 0:
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    # distance는 시작 노드를 1로 잡았으므로 -1
    answer = distance[G] - 1 if distance[G] else 0

    print(f"#{tc} {answer}")