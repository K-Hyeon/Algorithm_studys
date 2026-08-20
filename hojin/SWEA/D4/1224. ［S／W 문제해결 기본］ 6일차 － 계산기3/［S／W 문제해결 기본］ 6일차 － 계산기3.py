T=10
def isnum(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for test_case in range(1,T+1):
    result = 0
    length = int(input())
    expression = input()

    priority = ['(',')','+', '*']
    op_stack = []
    stack = []
    back_expression = ""
    for c in expression:
        # print(c, op_stack, back_expression)
        if isnum(c):
            back_expression += c
        #연산자일때
        else:
            if c not in ('(',')'):
            #연산자 우선순위가 top보다 크면 push, 작으면 출력후 pop
                #연산자 스택이 연산자가 있을때
                if op_stack:
                    #현재 연산자가 top보다 우선순위가 큼
                    if priority.index(c) > priority.index(op_stack[-1]):
                        op_stack.append(c)
                    #top에 있는 연산자가 현재 연산자보다 크거나 같음
                    else:
                        #그러면 스택이 비거나 현재 연산자보다 우선순위가 큰 연산자가 나올때까지 pop하고 출력
                        while op_stack:
                            if priority.index(c) > priority.index(op_stack[-1]):
                                break
                            back_expression += op_stack.pop()
                        op_stack.append(c)
                else:
                    op_stack.append(c)
            #괄호이면
            else:
                #닫는괄호
                if c == ')':
                    while op_stack:
                        if op_stack[-1] == '(':
                            op_stack.pop()
                            break
                        op = op_stack.pop()
                        back_expression += op
                #여는 괄호
                else:
                    op_stack.append(c)

    while op_stack:
        back_expression += op_stack.pop()

    # print(back_expression)
    #이제 계산
    for c in back_expression:
        #숫자면 스택에 저장
        if isnum(c):
            stack.append(c)
        #연산자면
        else:
            if c == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif c == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)

    result = stack.pop()
    print(f'#{test_case} {result}')