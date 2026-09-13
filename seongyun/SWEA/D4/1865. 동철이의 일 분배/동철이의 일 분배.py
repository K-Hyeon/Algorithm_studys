def solve():
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]

    dp = [0.0] * (1 << N)
    dp[0] = 1.0

    for mask in range(1 << N):
        if dp[mask] == 0:
            continue

        idx = bin(mask).count('1')
        if idx == N:
            continue

        for j in range(N):
            if not (mask & (1 << j)):
                next_mask = mask | (1 << j)
                dp[next_mask] = max(dp[next_mask], dp[mask] * prob[idx][j] / 100)

    return f"{dp[(1 << N) - 1] * 100:.6f}"


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")