T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    interest = list(input().strip())
    record = input()
    interest_cnt = [0] * len(interest)
    for c in record:
        for i in range(len(interest)):
            if interest[i] == c:
                interest_cnt[i] += 1
    result = max(interest_cnt)
    print(f'#{test_case} {result}')