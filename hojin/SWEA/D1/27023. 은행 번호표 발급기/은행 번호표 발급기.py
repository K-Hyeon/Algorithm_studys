from collections import deque
T = int(input())
for test_case in range(1,T+1):
    result = []
    m = int(input())
    orders = list(map(int, input().split()))
    num = 1
    queue = deque()
    for order in orders:
        if order == 1:
            queue.appendleft(num)
            num += 1
        elif order == 2:
            result.append(queue.pop())
    print(f"#{test_case}", end="")
    [print(f" {item}", end="") for item in result]
    print()