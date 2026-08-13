def solve():
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]

    homes = [(r, c) for r in range(N) for c in range(N) if town[r][c] == 1]

    max_home = 0
    cost = [k * k + (k - 1) * (k - 1) for k in range(N + 2)]

    for r in range(N):
        for c in range(N):
            dist_cnt = [0] * (2 * N - 1)
            for hr, hc in homes:
                d = abs(r - hr) + abs(c - hc)
                dist_cnt[d] += 1

            covered_homes = 0
            for k in range(1, N + 2):
                covered_homes += dist_cnt[k - 1]

                if covered_homes * M >= cost[k]:
                    max_home = max(max_home, covered_homes)

    return max_home

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")
