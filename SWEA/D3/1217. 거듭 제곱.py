def func(N, M):
    if M == 1: return N
    else: return N * func(N, M-1)

T = 10
for test_case in range(1, T + 1):
    test_case = int(input())
    N, M = map(int, input().split())
    print(f"#{test_case} {func(N, M)}")
