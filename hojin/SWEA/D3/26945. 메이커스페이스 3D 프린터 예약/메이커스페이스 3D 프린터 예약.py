import heapq
T = int(input())

for tc in range(1,T+1):
    result = 0
    n = int(input())
    queue = []
    hour = [0] * 25

    for i in range(n):
        s, e = map(int, input().split())
        heapq.heappush(queue, (e,s))

    while queue:
        e, s = heapq.heappop(queue)
        #겹치면 건너뛰기
        if 1 in hour[s:e]:
            continue

        for i in range(s,e):
            hour[i] = 1
        result += 1

    print(f'#{tc} {result}')