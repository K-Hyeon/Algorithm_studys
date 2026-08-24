T = int(input())
for test_case in range(1,T+1):
    result = 0
    n, m, l = map(int, input().split())
    song_list = list(map(int, input().split()))
    for i in range(m):
        p, v = map(int, input().split())
        song_list.insert(p,v)
    result = song_list[l]
    print(f'#{test_case} {result}')