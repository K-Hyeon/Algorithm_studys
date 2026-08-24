from collections import deque
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    t = int(input())
    nums = list(map(int, input().split()))
    queue = deque(nums)
    num = 1
    while True:
        if num > 5:
            num = 1
        value = queue.popleft()
        mod = value-num
        if mod <= 0:
            queue.append(0)
            break
        else:
            queue.append(mod)
        num += 1
    print(f"#{test_case}", end="")
    [print(f" {item}", end="") for item in queue]
    print()