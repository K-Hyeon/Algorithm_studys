T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    count = 0
    def dfs(index, current_sum):
        global count
        
        if current_sum > K:
            return
            
        # 배열의 끝까지 모두 탐색한 경우
        if index == N:
            if current_sum == K:
                count += 1
            return
            
        # 1) 현재 숫자를 부분 수열의 합에 포함하는 경우
        dfs(index + 1, current_sum + A[index])
        
        # 2) 현재 숫자를 부분 수열의 합에 포함하지 않는 경우
        dfs(index + 1, current_sum)

    #탐색 시작
    dfs(0, 0)
    
    print(f"#{tc} {count}")


# T = int(input())

# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
    
#     count = 0
    
#     # 길이가 1부터 N까지 배열 만들기 
#     for length in range(1, N + 1):
#         for i in range(N - length + 1):
#             if sum(A[i:i+length]) == K:
#                 count += 1
                
#     print(f"#{tc} {count}")
