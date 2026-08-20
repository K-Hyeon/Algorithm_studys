T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sticks_laser = input()
    stack = []
    result = 0
    for i in range(len(sticks_laser)):
        #디버그용 print
        # print(c, stack)
        #닫는 괄호가 아니면 그냥  stack에 넣는다.
        if sticks_laser[i] == '(':
            stack.append(sticks_laser[i])
        #닫는괄호이면
        elif sticks_laser[i] == ')':
            #레이저든 막대기든 어차피 짝이니까 하나는 뽑아야함
            stack.pop()
            #레이저이면
            if sticks_laser[i-1] == '(':
                result += len(stack)
            else:
                result += 1



    print(f'#{test_case} {result}')

