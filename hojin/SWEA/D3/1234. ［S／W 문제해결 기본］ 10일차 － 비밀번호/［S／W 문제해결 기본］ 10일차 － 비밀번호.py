T = 10
for test_case in range(1,T+1):
    n, numbers = input().split()
    result = 0
    stack = []
    for num in numbers:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    result = "".join(stack)
    print(f'#{test_case} {result}')