import math
from collections import deque
T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = list(input().split())
    queue_front = deque(arr[:math.ceil(n / 2)])
    queue_back = deque(arr[math.ceil(n / 2):n])
    result = ""
    while True:
        if not queue_front and not queue_back:
            break
        if queue_front:
            result += queue_front.popleft() + " "
        if queue_back:
            result += queue_back.popleft() + " "
    print(f'#{test_case} {result}')