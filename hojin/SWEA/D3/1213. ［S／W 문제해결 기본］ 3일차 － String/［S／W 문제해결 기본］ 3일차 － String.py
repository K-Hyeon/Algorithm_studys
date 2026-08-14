T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    search = input()
    sentence = input()
    result = 0
    #문장을 돌면서
    for i in range(len(sentence)):
        #search
        if search == sentence[i:i+len(search)]:
            result += 1
            
    print(f'#{test_case} {result}')
            