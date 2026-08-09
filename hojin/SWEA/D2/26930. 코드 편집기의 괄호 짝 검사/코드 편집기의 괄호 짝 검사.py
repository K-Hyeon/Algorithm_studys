T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 문자열에 들어있는 괄호는 무시하고 짝 맞추기
# 괄호의 종류는 소괄호 or 중괄호
for test_case in range(1, T + 1):
    open_paren = ['(','{']
    close_paren = [')','}']
    isStr = False
    result = 1
    line = input()
    stack = []
    for c in line:
        if c == '\'':
            isStr = not isStr
        if not isStr:
            if c in open_paren:
                stack.append(c)
            elif c in close_paren:
                if not stack:
                    result = 0
                    break
                elif (c == ')' and stack[-1] == '(') or (c == '}' and stack[-1] == '{'):
                    stack.pop()
                    

    if stack:
        result = 0

    print(f"#{test_case} {result}")