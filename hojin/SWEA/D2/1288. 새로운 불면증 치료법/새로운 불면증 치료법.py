T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #n을 배수로 곱해가면서 0부터 9까지의 숫자를 모두 보면 끝낸다.
    n = int(input())
    visit = {0,1,2,3,4,5,6,7,8,9}
    cnt = 0
    while visit:
        cnt += 1
        mul = n * cnt
        num_set = {int(i) for i in str(mul)}
        for num in num_set:
            if num in visit:
                visit.remove(num)

    result = n*cnt
    print(f"#{test_case} {result}")