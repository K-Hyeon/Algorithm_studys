def check(cells, D, W, K):
    if K == 1:
        return True
    
    for c in range(W):
        cnt = 1
        for r in range(1, D):
            if cells[r][c] == cells[r - 1][c]:
                cnt += 1
                if cnt == K:
                    break
            else:
                cnt = 1
        else:
            return False
    return True


def dfs(n, cells, isA, row, D, W, K, cur_min):
    if n >= cur_min:
        return n

    tmp = cells[row][:]
    cells[row] = [0] * W if isA else [1] * W

    if check(cells, D, W, K):
        cells[row] = tmp
        return n

    res = cur_min
    for i in range(row + 1, D):
        res = min(dfs(n + 1, cells, True, i, D, W, K, res), res)
        res = min(dfs(n + 1, cells, False, i, D, W, K, res), res)

    cells[row] = tmp
    return res
        

def solve():
    D, W, K = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(D)]

    if check(cells, D, W, K):
        return 0

    ans = K
    for i in range(D):
        ans = min(ans, dfs(1, cells, True, i, D, W, K, ans))
        ans = min(ans, dfs(1, cells, False, i, D, W, K, ans))
    return ans

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")