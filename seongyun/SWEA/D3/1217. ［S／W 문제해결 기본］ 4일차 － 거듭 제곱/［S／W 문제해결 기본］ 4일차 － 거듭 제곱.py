def power(n, i):
    if i == M:
        return n
    return power(n * N, i + 1)

for test_case in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    print(f"#{test_case} {power(N, 1)}")