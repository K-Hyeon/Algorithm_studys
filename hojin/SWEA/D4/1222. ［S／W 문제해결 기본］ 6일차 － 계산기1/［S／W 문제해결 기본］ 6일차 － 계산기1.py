T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    length = int(input())
    expression = input()
    back_expression = ""
    stack = []
    for c in expression:
        if c == '+':
            if stack:
                op = stack[-1]
                stack.pop()
                back_expression += op
            stack.append(c)
        else:
            back_expression += c
    if stack:
        back_expression += stack[-1]
        stack.pop()
    for c in back_expression:
        if c != '+':
            stack.append(c)
        else:
            while stack:
                val = stack[-1]
                stack.pop()
                result += int(val)
    print(f'#{test_case} {result}')