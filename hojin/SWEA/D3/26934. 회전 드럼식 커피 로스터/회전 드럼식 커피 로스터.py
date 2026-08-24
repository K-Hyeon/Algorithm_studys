from collections import deque
T = int(input())
for test_case in range(1,T+1):
    result = 0
    n, m = map(int, input().split())
    water_list = list(map(int, input().split()))
    queue = deque()
    #큐 초기화
    for i in range(n):
        #번호, 수분량으로 넣는다
        queue.append((i+1,water_list[i]))
    #현재 인덱스
    cur_index = n-1

    #큐 크기가 1이 되면 종료
    while len(queue) > 1:
        # print(queue)
        num, water = queue.popleft()
        mod = water // 2

        if mod == 0:
            if cur_index < m - 1:
                cur_index += 1
                queue.append((cur_index+1,water_list[cur_index]))
        else:
            queue.append((num, mod))
    result = queue.popleft()
    print(f'#{test_case} {result[0]}')