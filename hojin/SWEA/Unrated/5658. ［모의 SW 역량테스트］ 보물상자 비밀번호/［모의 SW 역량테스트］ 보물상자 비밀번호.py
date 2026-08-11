T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    numbers = input()
    #자리수이자 회전수 3
    digit = n//4
    rot = n//4

    hex_set = set()
    #회전
    for _ in range(rot):
        #생성한 수를 집합에 넣기
        for i in range(0,n,digit):
            #그냥 정수형으로 넣음
            num = int("".join(numbers[i:i+digit]), 16)
            hex_set.add(num)
        #다 넣었으면 1회 회전
        numbers = numbers[1:]+numbers[0]
    result_list = sorted(list(hex_set), reverse=True)
    print(f'#{test_case} {result_list[k-1]}')