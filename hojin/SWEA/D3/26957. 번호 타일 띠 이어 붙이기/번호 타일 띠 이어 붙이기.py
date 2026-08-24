T = int(input())
for test_case in range(1,T+1):
    n, m = map(int, input().split())
    result = []
    for _ in range(m):
        ddi = list(map(int, input().split()))
        if not result:
            result += ddi
        else:
            isContinue = False
            #기준값은 맨왼쪽 즉 ddi의 인덱스 0번이고 이거보다 result에서 큰 값 왼쪽에 끼운다.
            for i in range(len(result)):
                if result[i] > ddi[0]:
                    result = result[:i]+ddi+result[i:len(result)]
                    isContinue = True
                    break
            if isContinue: continue
            #다돌았는데 찾지 못하면 맨 뒤에 붙임
            result = result + ddi



    #오른쪽 끝부터 거꾸로 10개 읽기
    result = result[::-1][:10]
    print(f'#{test_case}', end="")
    [print(f' {item}', end="") for item in result]
    print()
