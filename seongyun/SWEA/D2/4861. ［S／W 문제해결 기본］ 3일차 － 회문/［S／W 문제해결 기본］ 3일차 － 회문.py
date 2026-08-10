def is_palindrome(board, r, c, M):
    left = c
    right = c + M - 1
    
    while left < right:
        if board[r][left] != board[r][right]:
            return False
        left += 1
        right -= 1
    return True

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    board_t = list(zip(*board))

    ans = ""
    is_find = False
    for r in range(N):
        for c in range(N - M + 1):
            if is_palindrome(board, r, c, M):
                ans =  "".join(board[r][c : c + M])
                is_find = True
                break
            if is_palindrome(board_t, r, c, M):
                ans = "".join(board_t[r][c : c + M])
                is_find = True
                break
        if is_find:
            break      

    print(f"#{test_case} {ans}")
