T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    result = 0
    matrix = [input().strip() for _ in range(8)]
    matrix = list(map(list, zip(*matrix[::-1])))
    for _ in range(2):
        for row in matrix:
            for i in range(8-length+1):
                sub = row[i:i+length]
                sub_rev = sub[::-1]
                if sub == sub_rev:
                    result += 1
        matrix = list(map(list, zip(*matrix[::-1])))



    print(f"#{test_case} {result}")