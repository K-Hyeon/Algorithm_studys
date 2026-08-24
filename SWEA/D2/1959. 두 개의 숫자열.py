T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_value = 0
    if N >= M : 
        for i in range(N-M+1):
            value = 0
            for j in range(M):
                value += A[i+j] * B[j]
            if value > max_value: max_value = value
    else:
        for i in range(M-N+1): # 3
            value = 0
            for j in range(N): # 3
                value += A[j] * B[i+j]
            if value > max_value: max_value = value
    print(f"#{test_case} {max_value}")
