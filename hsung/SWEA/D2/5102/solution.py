import sys
sys.stdin =open("5102/sample_input.txt", "r")

from collections import defaultdict, deque
test_case = int(input())

def bfs(graph, start, end):
    queue = deque([(start, 0)]) # 현재 노드와 이동거리 저장
    visited = set([start])
    
    while queue:
        current, dist = queue.popleft()

        if current == end:
            return dist
        
        for next_node in graph[current]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, dist + 1))
    return 0
        

for tc in range(test_case):
    N, E = map(int, input().split()) #전체 노드수 N , 엣지 수 E
    # print(f"start : {S} destination : {G}")
    graph  = defaultdict(list)
        
    for _ in range(E):
         node1 , node2 = map(int, input().split())
         graph[node1].append(node2)
         graph[node2].append(node1)
    S, G = map(int, input().split()) # 시작 노드 S, 마지막 노드 G
    cnt_to_end = bfs(graph, S, G)
    print(f"#{tc + 1} {cnt_to_end}")