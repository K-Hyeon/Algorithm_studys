T = int(input())
for test_case in range(1, T + 1):
    arr = input().strip()
    
    while any((i+i) in arr for i in arr):
        for i in arr:
            arr = arr.replace(i+i, "")
    print(f"#{test_case} {len(arr)}")
