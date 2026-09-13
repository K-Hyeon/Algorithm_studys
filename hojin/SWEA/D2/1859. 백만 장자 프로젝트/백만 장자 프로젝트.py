T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = arr[-1]
    arr = arr[::-1]
    result = 0
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            result += max_val - arr[i]
    print(f"#{test_case} {result}")