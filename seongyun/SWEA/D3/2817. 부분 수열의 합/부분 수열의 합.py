def dfs(idx, N, K, k, nums):
    if k == K:
        return 1
    
    if k > K:
        return 0
    
    if idx == N:
        return 0
    
    include = dfs(idx + 1, N, K, k + nums[idx], nums)
    exclude = dfs(idx + 1, N, K, k, nums)
    return include + exclude


def solve():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    
    return dfs(0, N, K, 0, nums)
    

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")