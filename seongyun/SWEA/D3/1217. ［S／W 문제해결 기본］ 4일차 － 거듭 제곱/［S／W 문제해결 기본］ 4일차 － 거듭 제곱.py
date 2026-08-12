def power(n, i, N, M):
    if i == M:
        return n
    return power(n * N, i + 1, N, M)

def solve():
    N, M = map(int, input().split())
    return power(1, 0, N, M)

for test_case in range(1, 11):
    T = int(input())
    print(f"#{test_case} {solve()}")