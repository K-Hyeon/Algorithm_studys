T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    walk = list(map(int,input().split()))
    most = 0
    least = sum(walk)
    for i in range(n-m+1):
        suum=0
        for j in range(m):
            suum += walk[i+j]

        if suum > most : most = suum
        if suum < least : least = suum
    print(f"#{test_case} {most-least}")