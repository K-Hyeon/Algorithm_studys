def check(x, y, isRow):
    if isRow:
        tmp = board[x][y:(y + M)]
    else:
        tmp = [board[k][y] for k in range(x, x + M)]

    return (tmp == tmp[::-1])

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]

    ans_pos = (0, 0, False)
    isFind = False
    for i in range(N):
        for j in range(N):
            if i + M - 1 < N and check(i, j, False):
                ans_pos = (i, j, False)
                isFind = True
                break
            if j + M - 1 < N and check(i, j, True):
                ans_pos = (i, j, True)
                isFind = True
                break
        if isFind:
            break

    if ans_pos[2]:
        ans = board[ans_pos[0]][ans_pos[1]:(ans_pos[1] + M)]
    else:
        ans = [board[k][ans_pos[1]] for k in range(ans_pos[0], ans_pos[0] + M)]
    print(f"#{test_case} {''.join(ans)}")
