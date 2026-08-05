from collections import deque

for test_case in range(1, 11):
    t = int(input())
    q = deque(map(int, input().split()))
    is_finished = False
    while not is_finished:
        for i in range(1, 6):
            tmp = max(0, q.popleft() - i)
            q.append(tmp)
            if tmp == 0:
                is_finished = True
                break

    q = map(str, q)
    print(f"#{test_case} {' '.join(q)}")
    