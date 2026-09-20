def solve():
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    isFixed = [False] * N

    max_prob = 0
    def dfs(idx, cur_prob):
        nonlocal max_prob

        if idx == N:
            max_prob = max(max_prob, cur_prob)
            return

        if cur_prob <= max_prob:
            return

        for i in range(N):
            if not isFixed[i]:
                isFixed[i] = True
                dfs(idx + 1, cur_prob * prob[idx][i] / 100)
                isFixed[i] = False

    dfs(0, 1)
    return f"{max_prob * 100 :.6f}"


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")