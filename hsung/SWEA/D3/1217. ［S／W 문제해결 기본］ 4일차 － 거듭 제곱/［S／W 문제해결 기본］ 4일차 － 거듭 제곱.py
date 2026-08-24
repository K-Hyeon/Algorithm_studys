def pow(N,M):
    if M == 1:
        return N
    else: 
        return pow(N, M-1)*N

for _ in range(10):
    t =int(input())
    N, M  = map(int, input().split())
    print(f"#{t} {pow(N,M)}")