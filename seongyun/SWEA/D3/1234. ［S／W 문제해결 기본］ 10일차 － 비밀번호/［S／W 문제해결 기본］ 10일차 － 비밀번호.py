for test_case in range(1, 11):
    N, text = input().split()
    N = int(N)
    stack = []
    for c in text:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    print(f"#{test_case} {''.join(stack)}")
    