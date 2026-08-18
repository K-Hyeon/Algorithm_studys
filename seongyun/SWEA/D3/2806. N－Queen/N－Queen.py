def recursive(row, N, visited_col, visited_diag1, visited_diag2):
    if row == N:
        return 1

    cnt = 0
    for col in range(N):
        if not visited_col[col] and not visited_diag1[row + col] and not visited_diag2[row - col + N]:
            visited_col[col] = True
            visited_diag1[row + col] = True
            visited_diag2[row - col + N] = True

            cnt += recursive(row + 1, N, visited_col, visited_diag1, visited_diag2)

            visited_col[col] = False
            visited_diag1[row + col] = False
            visited_diag2[row - col + N] = False

    return cnt
        

def solve():
    N = int(input())

    visited_col = [False] * N
    visited_diag1 = [False] * (2 * N)
    visited_diag2 = [False] * (2 * N)
    
    return recursive(0, N, visited_col, visited_diag1, visited_diag2)


T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")
