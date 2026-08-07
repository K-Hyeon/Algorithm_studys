T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    arr = []
    
    arr.append(0)
    for num in nums:
        arr.append(num)
        i = len(arr) - 1
        while i > 1 and arr[i] < arr[i // 2]:
            arr[i], arr[i // 2] = arr[i // 2], arr[i]
            i //= 2
    
    i = (len(arr) - 1) // 2
    ans = []
    while i > 0:
        ans.append(arr[i])
        i //= 2
    
    print(f"#{t} {sum(ans)}")
    