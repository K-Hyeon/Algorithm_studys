from collections import deque

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접 리스트
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)  # 양방향

    S, G = map(int, input().split())

    # 각 역까지의 이동 구간 수
    distance = [0] * (V + 1)

    queue = deque([S])
    distance[S] = 1

    while queue:
        current = queue.popleft()

        if current == G:
            break

        for next_node in graph[current]:
            if distance[next_node] == 0:
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    # distance[S]를 1로 시작했기 때문에
    # 실제 이동 구간 수는 -1
    answer = distance[G] - 1 if distance[G] else 0

    print(f'#{tc} {answer}')