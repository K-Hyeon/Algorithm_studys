T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    max_val = float('-inf')
    for _ in range(2):
        for row in matrix:
            sum_val = sum(row)
            max_val = max(max_val,sum_val)
        matrix = list(map(list, zip(*matrix)))
    
    #대각선 합
    diag_sum = 0
    diag_sum2 = 0
    for i in range(100):
        diag_sum += matrix[i][i]
        diag_sum2 += matrix[i][100-1-i]
    
    max_val = max(max_val, diag_sum, diag_sum2)
    print(f"#{test_case} {max_val}")