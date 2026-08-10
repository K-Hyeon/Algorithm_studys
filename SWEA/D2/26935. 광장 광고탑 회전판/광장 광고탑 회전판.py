T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N:광고판의 개수, M: 회전 횟수
    arr = list(map(int, input().split())) # N개의 누적 조회수
    
    print(f'#{test_case} {arr[M%N]}')