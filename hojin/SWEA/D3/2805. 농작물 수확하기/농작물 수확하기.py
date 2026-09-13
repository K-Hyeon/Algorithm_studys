T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    mid = n//2
    matrix = [input() for _ in range(n)]

    benefit = 0
    for i in range(n):
        if i <= mid:
            for j in range(mid-i, mid+i+1):
                benefit += int(matrix[i][j])
        else:
            for j in range(i-mid, n-(i-mid)):
                benefit += int(matrix[i][j])
    print(f'#{test_case} {benefit}')