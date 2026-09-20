T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 무조건 A가 더 짧은 배열이 되도록 세팅
    if N > M:
        N, M = M, N
        A, B = B, A
        
    max_sum = -999 #정도면 안전한 듯? 
    
    for i in range(M - N + 1):
        current_sum = 0
        for j in range(N):
            current_sum += A[j] * B[i + j]
           
        if current_sum > max_sum:
            max_sum = current_sum
            
    print(f"#{t} {max_sum}")