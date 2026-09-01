T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    matrix = [list(map(int,input().split())) for _ in range(n)]
    max_val = 0
    for row in matrix:
        cnt = 0
        for item in row:
            if item == 1:
                cnt += 1
            else:
                if max_val < cnt:
                    max_val = cnt
                cnt = 0
                continue
        if max_val < cnt:
            max_val = cnt
    matrix_col = list(map(list, zip(*matrix[::-1])))
    for row in matrix_col:
        cnt = 0
        for item in row:
            if item == 1:
                cnt += 1
            else:
                if max_val < cnt:
                    max_val = cnt
                cnt = 0
                continue
        if max_val < cnt:
            max_val = cnt
    print(f'#{test_case} {max_val}')