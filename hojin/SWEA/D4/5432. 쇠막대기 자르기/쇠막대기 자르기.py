T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sticks_laser = input()
    stack = []
    result = 0
    for c in sticks_laser:
        #디버그용 print
        # print(c, stack)
        #닫는 괄호가 아니면 그냥  stack에 넣는다.
        if c == '(':
            stack.append(c)
        #닫는괄호이면
        elif c == ')':
            #top을 확인해서 여는 괄호면 ()를 빼고 r을 넣는다.
            if stack[-1] == '(':
                stack.pop()
                stack.append('r')
            #top이 여는 괄호가 아니면 막대기안에 레이저가 몇개인지 센다
            #여는 괄호를 만날때까지 index를 줄인다.
            #여는 괄호 만나면 pop하고 레이저를 다시 넣는다.
            elif stack[-1] == 'r':
                cur_index = len(stack)-1
                laser_cnt = 0
                while True:
                    #현재 인덱스가 레이저이면 레이저 갯수를 센다.
                    if cur_index >=0 and stack[cur_index] == 'r':
                        laser_cnt += 1
                        cur_index -= 1
                    # 여는 괄호를 만나면
                    elif cur_index >=0 and stack[cur_index] == '(':
                        stack.pop(cur_index)
                        #레이저 갯수가 2개이면 3등분임
                        result += laser_cnt + 1
                        break


    print(f'#{test_case} {result}')

