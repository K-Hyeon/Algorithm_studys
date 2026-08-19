T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = input()
    opened = ['(', '[', '{', '<']
    closed = [')', ']', '}', '>']
    result = 1
    stack = []
    for c in arr:
        #닫는 괄호가 들어오면
        if c in closed:
            #stack top이 괄호짝이 맞는지 확인함
            if opened[closed.index(c)] == stack[-1]:
                #맞으면 stack에서 뺀다.
                stack.pop()
                continue
            else:
                result = 0
                break
        #닫는 괄호가 아니면
        else:
            stack.append(c)

    #다 돌았을 때 스택이 비어있어야 유효
    if not stack:
        stack = 0


    print(f'#{test_case} {result}')

