def solve():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    is_used = [False] * N
    res = float('inf')
    
    def dfs(idx, cur_sum):
        nonlocal res
        
        if cur_sum >= res:
            return
        
        if idx == N:
            res = cur_sum
            return
        
        for i in range(N):
            if not is_used[i]:
                is_used[i] = True
                dfs(idx + 1, cur_sum + board[idx][i])
                is_used[i] = False
    
    dfs(0, 0)
    return res
    

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")