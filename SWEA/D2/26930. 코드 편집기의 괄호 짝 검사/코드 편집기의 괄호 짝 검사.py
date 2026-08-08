T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    text = input()
    text = text.replace('&apos;', "'").replace('&quot;', "'")

    answer = 1
    temp = []
    for arr in text:
        # ', " 검사
        if temp and temp[-1] in ("'", '"'): 
            if arr not in ("'", '"'): continue
            else:
                temp.pop()
                continue
        
        # (, { 검사
        if arr in ('(', '{', "'", '"'): temp.append(arr)
        if arr in (')', '}'):
            if temp:
                next = temp.pop()
                if (arr == ')' and next == '(') or (arr == '}' and next == '{') : continue
                else: answer = 0
            else: answer = 0
    if temp :answer = 0

    print(f'#{test_case} {answer}')
    