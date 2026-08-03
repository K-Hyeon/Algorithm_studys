T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_result = 0
    if n <= m:
        #n이 3이고 m이 5이면
        for i in range(m-n+1):
            #3만큼 자름
            temp_b = b[i:i+n]
            sum = 0
            for j in range(n):
                sum += a[j] * temp_b[j]
            if sum > max_result: max_result = sum
    else:
        #반대로 n이5 m이 3
        for i in range(n - m + 1):
            # 3만큼 자름
            temp_a = a[i:i + m]
            sum = 0
            for j in range(m):
                sum += temp_a[j] * b[j]
            if sum > max_result: max_result = sum
    print(f"#{test_case} {max_result}")