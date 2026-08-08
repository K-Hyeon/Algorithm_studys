from collections import deque

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = deque(map(int, input().split()))
    
    while True:
        if arr[-1] == 0: break
        for i in range(1, 6):
            temp = arr.popleft()
            if temp - i > 0:
            	arr.append(temp-i)
            else:
                arr.append(0)
                break
    print(f"#{test_case} {' '.join(map(str, arr))}")
    #print(f"{N} {' '.join(arr)}")
          
        
        