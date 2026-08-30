T =int(input())
result = 0
def dfs(arr,start_idx,sum,k):
    global result
    if sum == k:
        result += 1
        return
    elif sum > k:
        return

    for i in range(start_idx+1,len(arr)):
        dfs(arr,i,sum+arr[i],k)
for t in range(1,T+1):
    result = 0

    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    for idx in range(len(A)):
        dfs(A,idx,A[idx],k)
    print(f'#{t} {result}')